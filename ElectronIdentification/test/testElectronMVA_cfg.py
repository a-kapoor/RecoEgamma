import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
from Configuration.AlCa.GlobalTag import GlobalTag
import os
process = cms.Process("ElectronMVANtuplizer")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2021_realistic_v3', '')#'106X_mcRun3_2023_realistic_v3', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2023_realistic_v3', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15','')

# File with the ID variables to include in the Ntuplizer
mvaVariablesFile = "RecoEgamma/ElectronIdentification/data/ElectronIDVariables.txt"

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring("file:ten_tau_reco_1000evt_miniAOD.root"))
                            fileNames = cms.untracked.vstring("/store/mc/Run3Summer19MiniAOD/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/270000/2A5317F8-5DC6-1E45-B946-A17A198B0B32.root"))

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

###Tau gen jet producer
process.load("PhysicsTools.JetMCAlgos.TauGenJets_cfi")

process.tauGenJets.GenParticles = cms.InputTag("prunedGenParticles")

process.TFileService = cms.Service("TFileService", fileName = cms.string(outputFile))

process.p = cms.Path(process.tauGenJets * process.egmGsfElectronIDSequence * process.ntuplizer)
