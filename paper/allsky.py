"""Make all-sky source overview plot.
"""
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
# plt.style.use('ggplot')
from astropy.table import Table
from astropy.visualization.mpl_normalize import simple_norm
from gammapy.image import SkyImage

def get_image():
    filename = '/Users/deil/code/gammapy-extra/datasets/fermi_2fhl/gll_psch_v08.fit.gz'
    image = SkyImage.read(filename)
    image.data = image.data.astype(float)
    sigma_pix = 3
    sigma_deg = sigma_pix * image.wcs_pixel_scale()[0]
    print('Smoothing by sigma = {} pix = {:.3f}'.format(sigma_pix, sigma_deg))
    image = image.smooth('gauss', sigma_pix)
    return image

def plot_image(image):
    
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], projection=image.wcs)
    
    ax.set_xlim(-0.5, image.data.shape[1] - 0.5)
    ax.set_ylim(-0.5, image.data.shape[0] - 0.5)
    
    norm = simple_norm(image.data,
        stretch='power', power=0.4,
        min_cut=0, max_cut=0.5,
    )
    print('image data max ', image.data.max())
    
    ax.imshow(image.data,
        origin='lower', norm=norm,
        cmap=plt.cm.gist_heat,
        interpolation='none',
    )

    plt.axis('off')


def get_gammacat():
    # TODO: change to gamma-cat when we have a first FITS version
    filename = '/Users/deil/code/gamma-cat/other_cats/tgevcat/tgevcat.ecsv'
    cat = Table.read(filename, format='ascii.ecsv')
    return cat

def plot_gammacat(cat):
    ax = plt.gca()
    x = cat['GLON'].data
    y = cat['GLAT'].data
    ax.scatter(x, y, s=50,
        edgecolor='white',
        # facecolor doesn't work with EPS, which is what we use for LaTeX
        facecolor='none',
        linewidth=1.0,
        # alpha=,
        transform=ax.get_transform('world')
    )

def main():
    image = get_image()
    plot_image(image)

    gammacat = get_gammacat()
    plot_gammacat(gammacat)

    fig = plt.gcf()

    filename = 'allsky.png'
    print('Writing ', filename)
    fig.savefig(filename, dpi=300)

    filename = 'allsky.pdf'
    print('Writing ', filename)
    fig.savefig(filename)


if __name__ == '__main__':
    main()
