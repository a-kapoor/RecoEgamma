from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
from copy import deepcopy
import os
 
def submit(config):
    res = crabCommand('submit', config = config)
    #save crab config for the future
    with open(config.General.workArea + "/crab_" + config.General.requestName + "/crab_config.py", "w") as fi:
        fi.write(config.pythonise_())

samples = [

        # ('/ZprimeToEE_M-3000_TuneCP5_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'ZprimeToEE_M-3000_TuneCP5_14TeV-pythia81'),

        # ('/ZprimeToEE_M-4000_TuneCP5_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'ZprimeToEE_M-4000_TuneCP5_14TeV-pythia8'),

        # ('/DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8'),

        # ('/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8'),

        # ('/GJet_Pt-10to40_DoubleEMEnriched_TuneCP5_14TeV_Pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'GJet_Pt-10to40_DoubleEMEnriched_TuneCP5_14TeV_Pythia8'),

        # ('/GJet_Pt-40toInf_DoubleEMEnriched_TuneCP5_14TeV_Pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'GJet_Pt-40toInf_DoubleEMEnriched_TuneCP5_14TeV_Pythia8'),

        # ('/QCD_Pt-10to30_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-10to30_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v3/MINIAODSIM',
        #  'QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt_15to20_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_15to20_bcToE_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt_20to30_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_20to30_bcToE_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt_30to80_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt_30to80_bcToE_TuneCP5_14TeV_pythia8'),

        ('/QCD_Pt_80to170_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
         'QCD_Pt_80to170_bcToE_TuneCP5_14TeV_pythia8_retry2'),

        # ('/QCD_Pt_170to250_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt_170to250_bcToE_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt_250toInf_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_rndm_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_250toInf_bcToE_TuneCP5_14TeV_pythia8'),

        # ('/TauGun_Pt-5to15_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'TauGun_Pt-5to15_14TeV-pythia8'),

        # ('/TauGun_Pt-15to500_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'TauGun_Pt-15to500_14TeV-pythia8')
]

if __name__ == "__main__":
    for dataset, name in samples:
 
        conf = config()
        submitVersion = "ntuple_PFID_Run3Summer21_forPR"
        mainOutputDir = '/store/group/phys_egamma/akapoor/%s' % submitVersion

        conf.General.workArea = 'crab_%s' % submitVersion
        conf.General.transferOutputs = True
        conf.JobType.pluginName  = 'Analysis'

        # Name of the CMSSW confuration file
        conf.JobType.psetName  = '/afs/cern.ch/user/a/akapoor/workspace/2020/EGamma_ggAnalysis_Ntuplizer/new/CMSSW_12_0_0/src/RecoEgamma/ElectronIdentification/test/testElectronMVA_cfg.py'
        conf.JobType.allowUndistributedCMSSW = True
        conf.Data.allowNonValidInputDataset = True
        
        conf.Data.inputDBS = 'global'
        conf.Data.publication = False
        
        #conf.Data.publishDataName =
        conf.Site.storageSite = 'T2_CH_CERN'
        
        conf.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
        conf.Data.splitting     = 'FileBased'
        conf.Data.unitsPerJob   = 20
        conf.Data.allowNonValidInputDataset = True
        

        conf.General.requestName = name
        conf.Data.inputDataset = dataset
        
        submit(conf) 
