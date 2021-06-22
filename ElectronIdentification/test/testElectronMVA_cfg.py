import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
from Configuration.AlCa.GlobalTag import GlobalTag
import os
process = cms.Process("ElectronMVANtuplizer")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun3_2021_realistic_v6', '')#'106X_mcRun3_2023_realistic_v3', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2023_realistic_v3', '')

# File with the ID variables to include in the Ntuplizer
mvaVariablesFile = "RecoEgamma/ElectronIdentification/data/ElectronIDVariables.txt"

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="QCDPt170to250bcToETuneCP513TeVpythia8_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_NewCode2021.root"

# os.system("dasgoclient --query=\"file dataset=/TauGun_Pt-15to500_14TeV-pythia8/Run3Summer19MiniAOD-2021Scenario_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="TauGun_Pt-15to500_14TeV_Run3Summer19MiniAOD-2021Scenario_106X_mcRun3_2021_NewCode2021.root"


# os.system("dasgoclient --query=\"file dataset=/DoublePion_E-50/Run3Summer19MiniAOD-2023ScenarioRECO_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files5.txt")
# outputFile="DoublePion_E-50-Run3Summer19MiniAOD-2023ScenarioRECO_106X_mcRun3_2023_versionFS.root"

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM instance=prod/global\" >files5.txt")
# outputFile="QCDPt30toInfDoubleEMEnrichedMGG-40to80TuneCP513TeVPythia8RunIIAutumn18MiniAOD102X_upgrade2018_realistic_v15-v2_versionFS.root"

#/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM

# os.system("dasgoclient --query=\"file dataset=/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v1/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="GJetPt20to40DoubleEMEnrichedMGG-80toInfTuneCP5_14TeV_Pythia8_Run3Summer19MiniAOD-2023Scenario106X_mcRun3_2023_realisticv3_newCode2021.root"

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ1.txt")
# outputFile="QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ1.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ2.txt")
# outputFile="QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ2.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ3.txt")
# outputFile="QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ3.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ4.txt")
# outputFile="QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ4.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ5.txt")
# outputFile="QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ5.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global site=$(dasgoclient --query='site dataset=/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM' | grep T2 | head -1)\" >filesQ6.txt")
# outputFile="QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('filesQ6.txt')]

# os.system("dasgoclient --query=\"file dataset=/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files2.txt")
# outputFile="GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_newCode2021.root"
# lines = [line.rstrip('\n') for line in open('files2.txt')]

# os.system("dasgoclient --query=\"file dataset=/QCD_Pt_15to7000_TuneCP5_Flat_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="QCD_Pt_15to7000_TuneCP5_Flat_14TeV_pythia8-Run3Summer19MiniAOD-106X_mcRun3_2023_versionFS_newCode2021.root"


# os.system("dasgoclient --query=\"file dataset=/Pionplusandminus_E10-100-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="Pionplusandminus_E10-100-gun-Run3Summer19MiniAOD-2021ScenarioForMUO_PionMatched.root"

# os.system("dasgoclient --query=\"file dataset= /QCD_Pt-15to7000_TuneCH2_Flat_13TeV_herwig7/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="QCD_Pt-15to7000_TuneCH2_Flat_13TeV_herwig7_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_NewCode2021.root"


# os.system("dasgoclient --query=\"file dataset=/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="QCD_Pt-120to170_EMEnriched_TuneCP514TeVpythia8Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2_NewCode2021.root"

# os.system("dasgoclient --query=\"file dataset=/DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v1/MINIAODSIM instance=prod/global\" >files.txt")
# outputFile="DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8-Run3Summer19MiniAOD-2023Scenario_NewCode2021+2021.root"
# lines = [line.rstrip('\n') for line in open('files.txt')]

#print(lines)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring("file:ten_tau_reco_1000evt_miniAOD.root"))
#                            fileNames = cms.untracked.vstring("/store/mc/Run3Summer19MiniAOD/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/270000/2A5317F8-5DC6-1E45-B946-A17A198B0B32.root"))

outputFile="output.root"

useAOD = False

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format  to be
# DataFormat.AOD or DataFormat.MiniAOD, as appropriate
if useAOD == True :
    dataFormat = DataFormat.AOD
else :
    dataFormat = DataFormat.MiniAOD

switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce
my_id_modules = [
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring16_GeneralPurpose_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring16_HZZ_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
                 ]

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

process.ntuplizer = cms.EDAnalyzer('ElectronMVANtuplizer',
        #
        eleMVAs             = cms.vstring(
                                          "egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp80",
                                          "egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90",
                                          "egmGsfElectronIDs:mvaEleID-Spring16-HZZ-V1-wpLoose",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp80",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wpLoose",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wpHZZ",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wp80",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wpLoose",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wp90",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp90",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp80",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wpLoose",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp90",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp80",
                                          "egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wpLoose",
                                          ),
        eleMVALabels        = cms.vstring(
                                          "Spring16GPV1wp80",
                                          "Spring16GPV1wp90",
                                          "Spring16HZZV1wpLoose",
                                          "Fall17noIsoV2wp80",
                                          "Fall17noIsoV2wpLoose",
                                          "Fall17noIsoV2wp90",
                                          "Fall17isoV2wpHZZ",
                                          "Fall17isoV2wp80",
                                          "Fall17isoV2wpLoose",
                                          "Fall17isoV2wp90",
                                          "Fall17noIsoV1wp90",
                                          "Fall17noIsoV1wp80",
                                          "Fall17noIsoV1wpLoose",
                                          "Fall17isoV1wp90",
                                          "Fall17isoV1wp80",
                                          "Fall17isoV1wpLoose",
                                          ),
        eleMVAValMaps        = cms.vstring(
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16GeneralPurposeV1RawValues",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16HZZV1Values",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16HZZV1RawValues",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV2Values",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17IsoV2Values",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17IsoV2RawValues",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17IsoV1Values",
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV1Values",
                                           ),
        eleMVAValMapLabels   = cms.vstring(
                                           "Spring16GPV1Vals",
                                           "Spring16GPV1RawVals",
                                           "Spring16HZZV1Vals",
                                           "Spring16HZZV1RawVals",
                                           "Fall17NoIsoV2Vals",
                                           "Fall17NoIsoV2RawVals",
                                           "Fall17IsoV2Vals",
                                           "Fall17IsoV2RawVals",
                                           "Fall17IsoV1Vals",
                                           "Fall17NoIsoV1Vals",
                                           ),
        eleMVACats           = cms.vstring(
                                           "electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV1Categories",
                                           ),
        eleMVACatLabels      = cms.vstring(
                                           "EleMVACats",
                                           ),
        #
                                   variableDefinition   = cms.string(mvaVariablesFile),
                                   ptThreshold = cms.double(5.0),
                                   #
                                   doEnergyMatrix = cms.bool(False), # disabled by default due to large size
                                   energyMatrixSize = cms.int32(2), # corresponding to 5x5
                                   ###gen tau jet collection
                                   genTauJetCollection = cms.InputTag("tauGenJets")
                               )
"""
The energy matrix is for ecal driven electrons the n x n of raw
rec-hit energies around the seed crystal.

The size of the energy matrix is controlled with the parameter
"energyMatrixSize", which controlls the extension of crystals in each
direction away from the seed, in other words n = 2 * energyMatrixSize + 1.

The energy matrix gets saved as a vector but you can easily unroll it
to a two dimensional numpy array later, for example like that:

>>> import uproot
>>> import numpy as np
>>> import matplotlib.pyplot as plt

>>> tree = uproot.open("electron_ntuple.root")["ntuplizer/tree"]
>>> n = 5

>>> for a in tree.array("ele_energyMatrix"):
>>>     a = a.reshape((n,n))
>>>     plt.imshow(np.log10(a))
>>>     plt.colorbar()
>>>     plt.show()
"""
###Tau gen jet producer
process.load("PhysicsTools.JetMCAlgos.TauGenJets_cfi")

process.tauGenJets.GenParticles = cms.InputTag("prunedGenParticles")

process.TFileService = cms.Service("TFileService", fileName = cms.string(outputFile))

process.p = cms.Path(process.tauGenJets * process.egmGsfElectronIDSequence * process.ntuplizer)


####Used to check the output collection name
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('myOutputFile.root'),
#                               SelectEvents = cms.untracked.PSet(
#                                   SelectEvents = cms.vstring("p")
#                            )
#                           )
#process.e = cms.EndPath(process.out)                                                                        
