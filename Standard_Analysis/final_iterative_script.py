from fermipy.gtanalysis import GTAnalysis
import matplotlib
matplotlib.use("agg")

gta = GTAnalysis("SMC_data2/config.yaml", logging={"verbosity": 3})
gta.load_roi("first_attempt")

model = {
    "SpatialModel": "PointSource",
    "SpectrumType": "PowerLaw",
    "Index": 2.0
}


gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.optimize()
gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_attempt")

gta.residmap("third_attempt", model=model, make_plots=True)
gta.tsmap("third_attempt", model=model, make_plots=True, multithread=True)

# first iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_01_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_01_after_adding_sources")

gta.residmap("third_iteration_01_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_01_after_adding_sources", model=model, make_plots=True, multithread=True)

# Second iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_02_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_02_after_adding_sources")

gta.residmap("third_iteration_02_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_02_after_adding_sources", model=model, make_plots=True, multithread=True)

# third iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_03_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_03_after_adding_sources")

gta.residmap("third_iteration_03_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_03_after_adding_sources", model=model, make_plots=True, multithread=True)

# fourth iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_04_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_04_after_adding_sources")

gta.residmap("third_iteration_04_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_04_after_adding_sources", model=model, make_plots=True, multithread=True)

# fifth iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_05_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_05_after_adding_sources")

gta.residmap("third_iteration_05_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_05_after_adding_sources", model=model, make_plots=True, multithread=True)


# sixth iteration

gta.delete_sources(distance=15.0, minmax_ts=[None, 1.0])
gta.delete_sources(distance=15.0, minmax_npred=[None, 1.0])

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_06_after_removing_weak_sources")

gta.find_sources(model=model, sqrt_ts_threshold=4.0, min_separation=0.2, tsmap_fitter="tsmap")

gta.free_sources(free=False)
gta.free_source("galdiff")
gta.free_source("isodiff")
gta.free_sources(distance=6.0, minmax_ts=[10, None], pars=["norm", "Prefactor"])
gta.free_sources(distance=4.0, minmax_ts=[100, None], pars=["Index"])
gta.free_source("4FGL J1713.5-3945e", pars=["norm", "Prefactor"])

gta.fit(optimizer="NEWMINUIT", min_fit_quality=3)
gta.write_roi("third_iteration_06_after_adding_sources")

gta.residmap("third_iteration_06_after_adding_sources", model=model, make_plots=True)
gta.tsmap("third_iteration_06_after_adding_sources", model=model, make_plots=True, multithread=True)


