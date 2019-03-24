from Style_Transfer.style_tools import *
from Style_Transfer.model import *

early_stopping = {
    'CONTENT_LOSS': float('inf'),
    'BEST_IMG': 0,
    'LAST_BEST': False,
}


def run_style_transfer(cnn, normalization_mean, normalization_std,
                       content_img, style_img, input_img, content_lyer,
                       style_lyer, num_steps, style_weight,
                       content_weight):
    """Run the style transfer."""
    print('Building the style transfer model. Epochs: %d' % num_steps)
    model, style_losses, content_losses = get_style_model_and_losses(cnn, normalization_mean, normalization_std,
                                                                     style_img, content_img, content_lyer, style_lyer)
    optimizer = get_input_optimizer(input_img)

    print('Optimizing..')
    run = [0]
    while run[0] < num_steps:

        def closure():
            # correct the values of updated input image
            input_img.data.clamp_(0, 1)

            optimizer.zero_grad()
            model(input_img)
            style_score = 0
            content_score = 0

            for sl in style_losses:
                style_score += sl.loss
            for cl in content_losses:
                content_score += cl.loss

            style_score *= style_weight
            content_score *= content_weight

            loss = style_score + content_score
            loss.backward()

            run[0] += 1
            if run[0] % 50 == 0:
                print("Epoch {}:".format(run))
                print('Style Loss: {:4f}; Content Loss: {:4f}'.format(
                    style_score.item(), content_score.item()))
                PARAMETERS['EARLY_STOPPING'].append([style_score.item(), content_score.item(), run[0]])
                if content_score.item() < early_stopping['CONTENT_LOSS']:
                    early_stopping['CONTENT_LOSS'] = content_score.item()
                    early_stopping['BEST_IMG'] = copy.deepcopy(input_img)

            if run[0] == PARAMETERS['STYLE_STEPS']:
                if content_score.item() < early_stopping['CONTENT_LOSS']:
                    early_stopping['LAST_BEST'] = True
                    early_stopping['CONTENT_LOSS'] = content_score.item()
                    early_stopping['BEST_IMG'] = copy.deepcopy(input_img)

            return style_score + content_score

        """(To use the LBGFS optimizer, it is necessary to pass into the step function a closure function which 
        “reevaluates the model and returns the loss”;
         we don’t need to do that with any other optimizer…go figure) """
        optimizer.step(closure)

    """early stopping"""
    if not early_stopping['LAST_BEST']:
        input_img = early_stopping['BEST_IMG']
        print("best content loss: %.2f" % early_stopping['CONTENT_LOSS'])

    # a last correction...
    input_img.data.clamp_(0, 1)
    return input_img


def style_transfer(content_img, style, k):
    style_img = image_loader(style)
    # content_img = image_loader(original)

    assert style_img.size() == content_img.size(), \
        "we need to import style and content images of the same size"

    # imshow(style_img, title='Style Image')


    # TODO play with model
    cnn = models.vgg13(pretrained=True).features.to(device).eval()
    # cnn = models.vgg16(pretrained=True).features.to(device).eval()
    # cnn = models.vgg19(pretrained=True).features.to(device).eval()
    # cnn = models.vgg19_bn(pretrained=True).features.to(device).eval()

    print(40 * '-')
    print("Training Neural Net with %d" % get_n_params(cnn))

    early_stopping['CONTENT_LOSS'] = float('inf')
    early_stopping['BEST_IMG'] = 0
    early_stopping['LAST_BEST'] = False

    cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

    # TODO play with layers
    content_layers_default = ['conv_4']
    style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']

    input_img = content_img.clone()
    # if you want to use white noise instead uncomment the below line:
    # input_img = torch.randn(content_img.data.size(), device=device)

    output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                content_img, style_img, input_img, content_layers_default,
                                style_layers_default, PARAMETERS['STYLE_STEPS'], PARAMETERS['STYLE_WEIGHTS'],
                                PARAMETERS['CONTENT_WEIGHTS'])

    # plt.figure()
    # imshow(output, title='Output Image')

    # plt.ioff()
    # plt.show()

    name = 'styled/' + k[:-4] + '.png'
    torchvision.utils.save_image(output, name)



if __name__ == "__main__":
    style_transfer()

