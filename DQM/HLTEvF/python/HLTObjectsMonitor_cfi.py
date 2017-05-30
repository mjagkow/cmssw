import FWCore.ParameterSet.Config as cms

hltObjectsMonitor4all = cms.EDAnalyzer('HLTObjectsMonitor',
    TopFolder = cms.string("HLT/Objects"),
    label     = cms.string("all"),
#    debug = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    TriggerResults    = cms.InputTag("TriggerResults","","HLT"),
    TriggerSummary    = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    beamspot          = cms.InputTag("hltOnlineBeamSpot"),
    caloJetBTags      = cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
    pfJetBTags        = cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
    muCandidates      = cms.InputTag("hltL3NoFiltersNoVtxMuonCandidates"),
    eleCandidates     = cms.InputTag("hltEgammaCandidates"),
    processName    = cms.string("HLT"),
    plots = cms.VPSet(
       cms.PSet(
           pathNAME = cms.string("HLT_DoubleMu4_3_Jpsi_Displaced"),
           moduleNAME = cms.string("hltDisplacedmumuFilterDoubleMu43Jpsi"),
           label  = cms.string("muon (low mass)"),
           xTITLE = cms.string("mass (low mass)"),
           etaBINNING  = cms.vdouble(-2.4,-2.1,-1.6,-1.2,-0.9,-0.3,-0.2,0.2,0.3,0.9,1.2,1.6,2.1,2.4),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.,11.,12.,14.,20.,40.,60.,80.,100.,120.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),           
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
       cms.PSet(
           pathNAME = cms.string("HLT_Ele105_CaloIdVT_GsfTrkIdT"),
           moduleNAME = cms.string("xxx"),
           label  = cms.string("electron (high-pT)"),
           xTITLE = cms.string("electron (high-pT)"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.,210.,220.,230.,240.,250.,260.,270.,280.,290.,300.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dzBINNING  = cms.vdouble(-2.0,-1.5,-1.0,-0.8,-0.6,-0.4,-0.2,-0.1,-0.05,-0.025,0.0,0.025,0.05,0.1,0.2,0.4,0.6,0.8,1.0,1.5,2.0),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.,220.,240.,260.,280.,300.,350.,400.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(True),
           displayInPrimary_dz       = cms.bool(True),
           displayInPrimary_dimass   = cms.bool(True),           
           doPlot2D     = cms.untracked.bool(True),
           doPlotETA    = cms.untracked.bool(True),
           doPlotMASS   = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17  = cms.untracked.bool(True),
           doPlotCSV    = cms.untracked.bool(False),
           doCALO       = cms.untracked.bool(False),
           doPF         = cms.untracked.bool(False),
           doPlotRazor  = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(True),
           doPlotDZ     = cms.untracked.bool(True),
           doPlotDiMass = cms.untracked.bool(True),
       ),
#       jetAK4 = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_PFJet200"),
           moduleNAME = cms.string("hltSinglePFJet200"),
           label  = cms.string("PF jet (AK4)"),
           xTITLE = cms.string("PF jet (AK4)"),
           etaBINNING    = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING     = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.,210.,220.,230.,240.,250.,300.,310.,320.,330.,340.,350.,360.,370.,380.,390.,400.,410.,420.,430.,440.,450.),
           phiBINNING    = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING   = cms.vdouble(),
           dxyBINNING    = cms.vdouble(),
           dzBINNING    = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),                      
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(False),
           doPF        = cms.untracked.bool(False),
           doPlotRazor = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
#       caloHT = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_HT650_DisplacedDijet80_Inclusive"),
           moduleNAME = cms.string("hltHT650"),
           label  = cms.string("CALO HT"),
           xTITLE = cms.string("CALO HT"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,100.,200.,300.,400.,500.,550.,600.,650.,700.,800.,850.,900.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(),
           dzBINNING = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),                      
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(False),
           doPF        = cms.untracked.bool(False),
           doPlotRazor = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
#       pfHT = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_PFHT750_4JetPt80"),
           moduleNAME = cms.string("hltPF4JetPt80HT750"),
           label  = cms.string("PF HT"),
           xTITLE = cms.string("PF HT"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,100.,200.,300.,400.,500.,550.,600.,650.,700.,800.,850.,900.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(),
           dzBINNING = cms.vdouble(),
           dimassBINNING = cms.vdouble(),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(False),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz       = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),                      
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(False),
           doPF        = cms.untracked.bool(False),
           doPlotRazor = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ    = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
#       bJetPF = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500"),
           moduleNAME = cms.string("hltBTagPFCSVp016SingleWithMatching"),
           label  = cms.string("PF b-tag"),
           xTITLE = cms.string("PF b-tag"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(),
           dzBINNING = cms.vdouble(),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(True),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz      = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),           
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(False),
           doPF        = cms.untracked.bool(True),
           doPlotRazor = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ    = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),
       ),
#       bJetCalo = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067"),
           moduleNAME = cms.string("hltBTagCaloCSVp067Single"),
           label  = cms.string("CALO b-tag"),
           xTITLE = cms.string("CALO b-tag"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(),
           dzBINNING = cms.vdouble(),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(True),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(False),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz      = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(True),                      
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(True),
           doPF        = cms.untracked.bool(False),
           doPlotRazor = cms.untracked.bool(False),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ    = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(True),           
       ),
#       Rsq = cms.PSet(
       cms.PSet(
           pathNAME = cms.string("HLT_RsqMR270_Rsq0p09_MR200"),
           moduleNAME = cms.string("hltRsqMR270Rsq0p09MR200"),
           label  = cms.string("RSQ"),
           xTITLE = cms.string("RSQ"),
           etaBINNING  = cms.vdouble(-2.5,-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0,2.5),
           ptBINNING   = cms.vdouble(0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.),
           phiBINNING  = cms.vdouble(-3.2,-3.,-2.8,-2.6,-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2),
           massBINNING = cms.vdouble(),
           dxyBINNING = cms.vdouble(),
           dzBINNING = cms.vdouble(),
           dimassBINNING = cms.vdouble(0.,2.0,4.0,6.0,8.0,10.,12.,14.,20.,40.,60.,70.,80.,84.,86.,88.,90.,92.,94.,96.,100.,120.,140.,160.,200.),
           displayInPrimary_eta      = cms.bool(True),
           displayInPrimary_phi      = cms.bool(True),
           displayInPrimary_pt       = cms.bool(True),
           displayInPrimary_mass     = cms.bool(False),
           displayInPrimary_energy   = cms.bool(False),
           displayInPrimary_csv      = cms.bool(True),
           displayInPrimary_etaVSphi = cms.bool(True),
           displayInPrimary_pt_HEP17 = cms.bool(True),
           displayInPrimary_pt_HEM17 = cms.bool(True),
           displayInPrimary_MR       = cms.bool(False),
           displayInPrimary_RSQ      = cms.bool(True),
           displayInPrimary_dxy      = cms.bool(False),
           displayInPrimary_dz      = cms.bool(False),
           displayInPrimary_dimass   = cms.bool(False),                      
           doPlot2D    = cms.untracked.bool(True),
           doPlotETA   = cms.untracked.bool(True),
           doPlotMASS  = cms.untracked.bool(False),
           doPlotENERGY = cms.untracked.bool(False),
           doPlotHEP17 = cms.untracked.bool(True),
           doPlotCSV   = cms.untracked.bool(False),
           doCALO      = cms.untracked.bool(True),
           doPF        = cms.untracked.bool(False),
           doPlotRazor = cms.untracked.bool(True),
           doPlotDXY    = cms.untracked.bool(False),
           doPlotDZ     = cms.untracked.bool(False),
           doPlotDiMass = cms.untracked.bool(False),           
       ),
    ),
)

from DQM.HLTEvF.HLTObjectsMonitor_EGM_cfi import *
from DQM.HLTEvF.HLTObjectsMonitor_B2G_cfi import *
from DQM.HLTEvF.HLTObjectsMonitor_TAU_cfi import *
from DQM.HLTEvF.HLTObjectsMonitor_SUS_cfi import *
from DQM.HLTEvF.HLTObjectsMonitor_MUO_cfi import *
#from DQM.HLTEvF.HLTObjectsMonitor_JME_cfi import *

hltObjectsMonitor4all.plots.extend(egmObjects)
hltObjectsMonitor4all.plots.extend(b2gObjects)
hltObjectsMonitor4all.plots.extend(tauObjects)
hltObjectsMonitor4all.plots.extend(susObjects)
hltObjectsMonitor4all.plots.extend(muoObjects)
#hltObjectsMonitor4all.plots.extend(jmeObjects)

hltObjectsMonitor4sus = cms.EDAnalyzer('HLTObjectsMonitor',
    TopFolder = cms.string("HLT/Objects"),
    label     = cms.string("susy"),
#    debug = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    TriggerResults    = cms.InputTag("TriggerResults","","HLT"),
    TriggerSummary    = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    beamspot          = cms.InputTag("hltOnlineBeamSpot"),
    caloJetBTags      = cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
    pfJetBTags        = cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
    muCandidates      = cms.InputTag("hltL3NoFiltersNoVtxMuonCandidates"),
    eleCandidates     = cms.InputTag("hltDoubleEle8CaloIdMGsfTrackIdMDphiFilter"),
    processName    = cms.string("HLT"),
    plots = cms.VPSet(
    )
)
hltObjectsMonitor4sus.plots.extend(susObjects)

from DQM.HLTEvF.HLTObjectsMonitor_EXO_cfi import *

hltObjectsMonitor4exo = cms.EDAnalyzer('HLTObjectsMonitor',
    TopFolder = cms.string("HLT/Objects"),
    label     = cms.string("exo"),
#    debug = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    TriggerResults    = cms.InputTag("TriggerResults","","HLT"),
    TriggerSummary    = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    beamspot          = cms.InputTag("hltOnlineBeamSpot"),
    caloJetBTags      = cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
    pfJetBTags        = cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
    muCandidates      = cms.InputTag("hltL3NoFiltersNoVtxMuonCandidates"),
    eleCandidates     = cms.InputTag("hltEgammaHollowTrackIso"),
    processName    = cms.string("HLT"),
    plots = cms.VPSet(
    )
)
hltObjectsMonitor4exo.plots.extend(exoObjects)

hltObjectsMonitor4exoDisplaced = cms.EDAnalyzer('HLTObjectsMonitor',
    TopFolder = cms.string("HLT/Objects"),
    label     = cms.string("exoDisplaced"),
#    debug = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    TriggerResults    = cms.InputTag("TriggerResults","","HLT"),
    TriggerSummary    = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    beamspot          = cms.InputTag("hltOnlineBeamSpot"),
    caloJetBTags      = cms.InputTag("hltCombinedSecondaryVertexBJetTagsCalo"),
    pfJetBTags        = cms.InputTag("hltCombinedSecondaryVertexBJetTagsPF"),
    muCandidates      = cms.InputTag("hltGlbTrkMuonCandsNoVtx"),
    eleCandidates     = cms.InputTag(""),
    processName    = cms.string("HLT"),
    plots = cms.VPSet(
    )
)
hltObjectsMonitor4exoDisplaced.plots.extend(exoDisplacedObjects)


hltObjectsMonitor = cms.Sequence(
    hltObjectsMonitor4all
    + hltObjectsMonitor4sus
    + hltObjectsMonitor4exo
    + hltObjectsMonitor4exoDisplaced
)
