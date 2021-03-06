(pn.ggplot(falcor, pn.aes(x='Bacterial_genotype', y='log10 Mc'))
    + pn.geom_point()
    + pn.facet_wrap('Phage', dir='v')
    + pn.geom_errorbar(pn.aes(ymin='log10 LBc', ymax='log10 UBc'), width=.2)
    + pn.theme_bw()
)