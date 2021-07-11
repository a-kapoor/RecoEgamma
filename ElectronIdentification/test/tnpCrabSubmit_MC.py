from CRABClient.UserUtilities import config #getUsernameFromSiteDB
import sys
config = config()

submitVersion = "ntuple_PFID_July"
mainOutputDir = '/store/group/phys_egamma/akapoor/ntuple_ForPFID_July/%s' % submitVersion

# config.General.transferLogs = False

config.General.transferOutputs = True
config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/afs/cern.ch/user/a/akapoor/workspace/2020/EGamma_ggAnalysis_Ntuplizer/CMSSW_10_6_3/src/RecoEgamma/ElectronIdentification/test/testElectronMVA_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.Data.allowNonValidInputDataset = True

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_CH_CERN'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 20
    config.Data.allowNonValidInputDataset = True
    
    
    # config.Data.inputDataset = '/ZprimeToTT_M3000_W30_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'ZprimeToTT_M3000_W30_TuneCP5_14TeV-madgraphMLM-pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    # config.Data.inputDataset = '/ZprimeToTT_M4000_W40_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'ZprimeToTT_M4000_W40_TuneCP5_14TeV-madgraphMLM-pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog_ondisknow'
    # submit(config)


    # config.Data.inputDataset = '/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    # config.Data.inputDataset = '/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v1/MINIAODSIM'
    # config.General.requestName = 'DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8_July2021newflaaddedclusterisog_ondisknow'
    # submit(config)

    
    # config.Data.inputDataset = '/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/TauGun_Pt-15to500_14TeV-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'TauGun_Pt-15to500_14TeV-pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/TauGun_Pt-15to500_14TeV-pythia8/Run3Summer19MiniAOD-2021Scenario_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'TauGun_Pt-15to500_14TeV-pythia8_2021'
    # submit(config)

    # config.Data.inputDataset = '/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v1/MINIAODSIM'
    # config.General.requestName = 'GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    # config.Data.inputDataset = '/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_14TeV_Pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_14TeV_Pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    # config.Data.inputDataset = '/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_14TeV_Pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/QCD_Pt_15to7000_TuneCP5_Flat_14TeV_pythia8/Run3Summer19MiniAOD-106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-15to7000_TuneCP5_Flat_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    config.Data.inputDataset = "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"
    config.General.requestName ="QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)

    config.Data.inputDataset = "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
    config.General.requestName ="QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)

    config.Data.inputDataset = "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"
    config.General.requestName ="QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)
    
    config.Data.inputDataset = "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
    config.General.requestName = "QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)

    config.Data.inputDataset = "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
    config.General.requestName = "QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)

    config.Data.inputDataset = "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"
    config.General.requestName = "QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8_July2021newflaaddedclusterisog"
    submit(config)
    

    # config.Data.inputDataset = '/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8'
    # submit(config)


    # config.Data.inputDataset = '/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8'
    # submit(config)


# #333333333333333333333333333333333333333

#     config.Data.inputDataset = '/Eleplusandminus_E1-10-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Eleplusandminus_E1-10-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Eleplusandminus_E10-100-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM'
#     config.General.requestName = 'Eleplusandminus_E10-100-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Eleplusandminus_E100-7000-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Eleplusandminus_E100-700-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)



#     config.Data.inputDataset = '/Muplusandminus_E1-10-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Muplusandminus_E1-10-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Muplusandminus_E10-100-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM'
#     config.General.requestName = 'Muplusandminus_E10-100-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Muplusandminus_E100-7000-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Muplusandminus_E100-700-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)

    
#     config.Data.inputDataset = '/Pionplusandminus_E1-10-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Pionplusandminus_E1-10-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Pionplusandminus_E10-100-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v2/MINIAODSIM'
#     config.General.requestName = 'Pionplusandminus_E10-100-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)


#     config.Data.inputDataset = '/Pionplusandminus_E100-7000-gun/Run3Summer19MiniAOD-2021ScenarioForMUO_106X_mcRun3_2021_realistic_v3-v1/MINIAODSIM'
#     config.General.requestName = 'Pionplusandminus_E100-700-gun-2021ScenarioForMUO_July2021newflaaddedclusterisog'
#     submit(config)



    # config.Data.inputDataset = '/QCD_Pt_1000to1400_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt_1000to1400_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)


    # config.Data.inputDataset = '/QCD_Pt_120to170_TuneCP5_14TeV_pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'QCD_Pt_120to170_TuneCP5_14TeV_pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    # config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8_July2021newflaaddedclusterisog'
    # submit(config)
    
    # config.Data.inputDataset = '/TTToHadronic_TuneCP5_14TeV-powheg-pythia8/Run3Summer19MiniAOD-2023Scenario_106X_mcRun3_2023_realistic_v3-v2/MINIAODSIM'
    # config.General.requestName = 'TTToHadronic_TuneCP5_14TeV-powheg-pythia8_July2021newflaaddedclusterisog'
    # submit(config)

    
