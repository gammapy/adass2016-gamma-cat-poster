"""Plot Crab pulsar and nebula spectral energy distribution (SED)."""
import numpy as np
import matplotlib
matplotlib.use('ps')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import astropy.units as u
from gammapy.datasets import load_crab_flux_points
from gammapy.spectrum import crab_flux

def plot_points():
    papers = [
        dict(tag='hegra', label='HEGRA (2004)'),
        dict(tag='magic', label='MAGIC (TODO)'),
        # 'veritas',
        dict(tag='hess', label='H.E.S.S. (2006)')
    ]
    table_all = load_crab_flux_points()
    # import IPython; IPython.embed()
    # Plot flux points
    for paper in papers:
        mask = table_all['paper'] == paper['tag']
        table = table_all[mask]
        print('paper: {}, points: {}'.format(paper, len(table)))
        x = table['energy'].to('TeV').data
        y = table['energy_flux'].data
        yerr_lo = table['energy_flux_err_lo'].data
        yerr_hi = table['energy_flux_err_hi'].data
        plt.errorbar(
            x, y, yerr=(yerr_lo, yerr_hi),
            linewidth=2,
            fmt='o', capsize=0,
            label=paper['label'],
        )


def plot_model():
    energy = np.logspace(-3, 2, 100) * u.TeV
    flux = u.Quantity(crab_flux(energy.to('TeV').value), 'cm^-2 s^-1 TeV^-1')
    energy_flux = (energy ** 2 * flux).to('erg cm^-2 s^-1')
    plt.plot(
        energy.value, energy_flux.value,
        label='Meyer (2010)',
        lw=2, alpha=0.7,
    )

def plot_format():
    plt.xlim((3e-3, 3e2))
    plt.ylim((8e-13, 2e-10))
    plt.xlabel('Energy (TeV)')
    plt.ylabel('E^2 dN/dE (erg cm^-2 s^-1)')
    plt.legend(loc='lower left')
    # plt.grid()
    plt.loglog()
    plt.tight_layout()
    
    import seaborn
    seaborn.despine()

def main():
    # fig = plt.figure(figsize=(6, 4))
    fig = plt.figure(figsize=(8, 5))
    
    plot_model()
    plot_points()
    plot_format()

    filename = 'spec.png'
    print('Writing ', filename)
    fig.savefig(filename, dpi=300)

    filename = 'spec.pdf'
    print('Writing ', filename)
    fig.savefig(filename)

    # filename = 'spec.eps'
    # print('Writing ', filename)
    # fig.savefig(filename)#, bbox_inches='tight')

if __name__ == '__main__':
    main()
