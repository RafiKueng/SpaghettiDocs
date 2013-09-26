# LMT\_GLS\_v4
# LMT\_v1.6.3
import matplotlib as mpl
import pylab as pl
glass_basis('glass.basis.pixels', solver='rwalk')
meta(author='c_cld', notes='using LensModellingTools')
setup_log('../tmp_media/009719/log.txt')
samplex_random_seed(0)
samplex_acceptance(rate=0.25, tol=0.15)
exclude_all_priors()
include_prior(
  'lens_eq',
  'time_delay',
  'profile_steepness',
  'J3gradient',
  'magnification',
  'hubble_constant',
  'PLsmoothness3',
  'shared_h',
  'external_shear',
)
hubble_time(13.700000)
globject('9719__ASW0007j6j')
zlens(0.500)
pixrad(8)
steepness(0,None)
smooth(2.00,include_central_pixel=False)
local_gradient(45.00)
symm()

shear(0.01)

A = 1.833, 0.733
B = -0.197, -1.805
source(1.000,
  A, 'min', 
  B, 'sad', None)
model(200)
savestate('../tmp_media/009719/state.txt')
env().make_ensemble_average()
env().arrival_plot(env().ensemble_average, only_contours=True,
                   colors='magenta', clevels=40)
env().overlay_input_points(env().ensemble_average)
pl.gca().axes.get_xaxis().set_visible(False)
pl.gca().axes.get_yaxis().set_visible(False)
pl.savefig('../tmp_media/009719/img1.png')
pl.close()
env().kappa_plot(env().ensemble_average, 0, with_contours=True,
                 clevels=20, vmax=1, with_colorbar=False)
pl.gca().axes.get_xaxis().set_visible(False)
pl.gca().axes.get_yaxis().set_visible(False)
pl.savefig('../tmp_media/009719/img2.png')
pl.close()
env().srcdiff_plot(env().ensemble_average)
env().overlay_input_points(env().ensemble_average)
pl.gca().axes.get_xaxis().set_visible(False)
pl.gca().axes.get_yaxis().set_visible(False)
pl.savefig('../tmp_media/009719/img3.png')
pl.close()
env().srcdiff_plot_adv(env().ensemble_average, night=True, upsample=8)
env().overlay_input_points(env().ensemble_average)
pl.savefig('../tmp_media/009719/img3_ipol.png', facecolor='black',
           edgecolor='none')
pl.close()
LMT={
 'svgViewport' : 500,
 'orgImgSize'  : 440,
 'pxScale'     : 0.16456,
 'orgPxScale'  : 0.18700,
 'gls_version' : 'v4',
 'lmt_version' : 'v1.6.3',
}