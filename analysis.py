from fermipy.gtanalysis import GTAnalysis

source = "4FGL J1713.5-3945e"
model = {"SpatialModel": "PointSource", "Index": 2.0, "SpectrumType": "PowerLaw"}

gta = GTAnalysis("config.yaml", logging={"verbosity": 3})
gta.setup()

gta.load_roi("/home/oslaf/hcummins/high_energy_analysis/HEA_fixed/SMC_data2_binsz/2.1-roi_after_fit.npy")

gta.free_source(source, free=True)
gta.fit(min_fit_quality=3, optimizer="NEWMINUIT")
print(gta.roi[source])

gta.write_roi("bin04_after_fit")

gta.delete_source(source)

gta.residmap("bin04_removed_source", model=model, make_plots=True)
gta.tsmap("bin04_removed_source", model=model, make_plots=True, multithread=False)

gta.residmap("bin04_removed_source_below100GeV", model=model, make_plots=True, loge_bounds=[None, 5])
gta.tsmap("bin04_removed_source_below100GeV", model=model, make_plots=True, loge_bounds=[None, 5], multithread=False)

gta.residmap("bin04_removed_source_above100GeV", model=model, make_plots=True, loge_bounds=[5, None])
gta.tsmap("bin04_removed_source_above100GeV", model=model, make_plots=True, loge_bounds=[5, None], multithread=False)
