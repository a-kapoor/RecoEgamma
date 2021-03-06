// -*- C++ -*-
//
// Package:    RecoEgamma/ElectronIdentification
// Class:      ElectronMVANtuplizer
//
/**\class ElectronMVANtuplizer ElectronMVANtuplizer.cc RecoEgamma/ElectronIdentification/plugins/ElectronMVANtuplizer.cc

 Description: Ntuplizer for training and testing electron MVA IDs.

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Jonas REMBSER
//         Created:  Thu, 22 Mar 2018 14:54:24 GMT
//
//


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/MVAVariableManager.h"
#include "RecoEgamma/EgammaTools/interface/MultiToken.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include <TTree.h>
#include <TFile.h>
#include <Math/VectorUtil.h>

///gen tau jets


//
// class declaration
//

class ElectronMVANtuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit ElectronMVANtuplizer(const edm::ParameterSet&);

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      void analyze(const edm::Event&, const edm::EventSetup&) override;

      // method called once each job just before starting event loop
      void beginJob() override {};
      // method called once each job just after ending the event loop
      void endJob() override {};

      int matchToTruth(reco::GsfElectron const& electron,
		     edm::View<reco::GenParticle> const& genParticles) const;

    
      float MultiClass(reco::GsfElectron const& electron);

    
      int matchToPion(reco::GsfElectron const& electron,
		     edm::View<reco::GenParticle> const& genParticles) const;

      int matchToPhoton(reco::GsfElectron const& electron,
		     edm::View<reco::GenParticle> const& genParticles) const;

      int matchToHadron(reco::GsfElectron const& electron,
		     edm::View<reco::GenParticle> const& genParticles) const;

      int matchToNeuPion(reco::GsfElectron const& electron,
		     edm::View<reco::GenParticle> const& genParticles) const;
    
      int matchToGenTauJets(reco::GsfElectron const& electron, 
			    edm::View<reco::Candidate>const&  genTauJet) const ;
  
      bool passElectronSel(reco::GsfElectron const& electron);
      // ----------member data ---------------------------

      //global variables
      int nEvent_;
      int nRun_;
      int nLumi_;
      int genNpu_;
      int vtxN_;

      // PF vars
      float eleIsMvaIsolated_;
      float eleIsMvaNonIsolated_;
      bool passElectronSelection_;

      // electron variables
      float eleQ_;
      int ele3Q_;
      float mclassEle_;
      int matchedToGenEle_;
      int matchedToGenPion_;
      int matchedToGenPhoton_;
      int matchedToGenNeuPion_;
      int matchedToHadron_;
      int matchedToGenTauJet_;

      std::vector<float> energyMatrix_;

      // gap variables
      bool eleIsEB_;
      bool eleIsEE_;
      bool eleIsEBEtaGap_;
      bool eleIsEBPhiGap_;
      bool eleIsEBEEGap_;
      bool eleIsEEDeeGap_;
      bool eleIsEERingGap_;

      int eleIndex_;

      // config
      const bool isMC_;
      const double deltaR_;
      const double ptThreshold_;

      // ID decisions objects
      const std::vector< std::string > eleMapTags_;
      std::vector< edm::EDGetTokenT< edm::ValueMap<bool> > > eleMapTokens_;
      const std::vector< std::string > eleMapBranchNames_;
      const size_t nEleMaps_;

      // MVA values and categories (optional)
      const std::vector< std::string > valMapTags_;
      std::vector< edm::EDGetTokenT<edm::ValueMap<float> > > valMapTokens_;
      const std::vector< std::string > valMapBranchNames_;
      const size_t nValMaps_;

      const std::vector< std::string > mvaCatTags_;
      std::vector< edm::EDGetTokenT<edm::ValueMap<int> > > mvaCatTokens_;
      const std::vector< std::string > mvaCatBranchNames_;
      const size_t nCats_;

      // Tokens for AOD and MiniAOD case
      const MultiTokenT<edm::View<reco::GsfElectron>>   src_;
      const MultiTokenT<std::vector<reco::Vertex>>      vertices_;
      const MultiTokenT<std::vector<PileupSummaryInfo>> pileup_;
      const MultiTokenT<edm::View<reco::GenParticle>>   genParticles_;
    //const MultiTokenT<edm::View<pat::PackedGenParticle>>   packedGenParticles_;
      const MultiTokenT<EcalRecHitCollection>           ebRecHits_;
      const MultiTokenT<EcalRecHitCollection>           eeRecHits_;

      // to hold ID decisions and categories
      std::vector<int> mvaPasses_;
      std::vector<float> mvaValues_;
      std::vector<int> mvaCats_;

      // To get the auxiliary MVA variables
      const MVAVariableHelper<reco::GsfElectron> variableHelper_;

      // other
      TTree* tree_;

      MVAVariableManager<reco::GsfElectron> mvaVarMngr_;
      const int nVars_;
      std::vector<float> vars_;

      const bool doEnergyMatrix_;
      const int energyMatrixSize_;

  ///gen taus
  edm::EDGetTokenT<edm::View<reco::Candidate> > genTauJetCollection_;
};

//
// constants, enums and typedefs
//

enum ElectronMatchType {
                        UNMATCHED,
                        TRUE_PROMPT_ELECTRON,
                        TRUE_ELECTRON_FROM_TAU,
			//TRUE_ELECTRON_FROMHADRONDECAY,
			TRUE_NON_PROMPT_ELECTRON,
                       }; // The last does not include tau parents


enum H_ElectronMatchType {
                        H_UNMATCHED,
                        H_TRUE_PROMPT_ELECTRON,
                        H_TRUE_ELECTRON_FROM_TAU,
			H_TRUE_ELECTRON_FROMHADRONDECAY,
			H_TRUE_NON_PROMPT_ELECTRON,
                       }; // The last does not include tau parents


enum P_ElectronMatchType {
                        P_UNMATCHED,
			P_FAR,
                        P_TRUE_PROMPT_ELECTRON,
                        P_TRUE_ELECTRON_FROM_TAU,
			P_TRUE_ELECTRON_FROMHADRONDECAY,
			P_TRUE_NON_PROMPT_ELECTRON,
                       }; // The last does not include tau parents


enum NP_ElectronMatchType {
                        NP_UNMATCHED,
			NP_FAR,
                        NP_TRUE_PROMPT_ELECTRON,
                        NP_TRUE_ELECTRON_FROM_TAU,
			NP_TRUE_ELECTRON_FROMHADRONDECAY,
			NP_TRUE_NON_PROMPT_ELECTRON,
                       }; // The last does not include tau parents



//
// constructors and destructor
//
ElectronMVANtuplizer::ElectronMVANtuplizer(const edm::ParameterSet& iConfig)
  : isMC_                  (iConfig.getParameter<bool>("isMC"))
  , deltaR_                (iConfig.getParameter<double>("deltaR"))
  , ptThreshold_           (iConfig.getParameter<double>("ptThreshold"))
  , eleMapTags_            (iConfig.getParameter<std::vector<std::string>>("eleMVAs"))
  , eleMapBranchNames_     (iConfig.getParameter<std::vector<std::string>>("eleMVALabels"))
  , nEleMaps_              (eleMapBranchNames_.size())
  , valMapTags_            (iConfig.getParameter<std::vector<std::string>>("eleMVAValMaps"))
  , valMapBranchNames_     (iConfig.getParameter<std::vector<std::string>>("eleMVAValMapLabels"))
  , nValMaps_              (valMapBranchNames_.size())
  , mvaCatTags_            (iConfig.getParameter<std::vector<std::string>>("eleMVACats"))
  , mvaCatBranchNames_     (iConfig.getParameter<std::vector<std::string>>("eleMVACatLabels"))
  , nCats_                 (mvaCatBranchNames_.size())
  , src_                   (consumesCollector(), iConfig, "src"         , "srcMiniAOD")
  , vertices_        (src_, consumesCollector(), iConfig, "vertices"    , "verticesMiniAOD")
  , pileup_          (src_, consumesCollector(), iConfig, "pileup"      , "pileupMiniAOD")
  , genParticles_    (src_, consumesCollector(), iConfig, "genParticles", "genParticlesMiniAOD")
    //, packedGenParticles_    (src_, consumesCollector(), iConfig, "packedGenParticles")
  , ebRecHits_       (src_, consumesCollector(), iConfig, "ebReducedRecHitCollection", "ebReducedRecHitCollectionMiniAOD")
  , eeRecHits_       (src_, consumesCollector(), iConfig, "eeReducedRecHitCollection", "eeReducedRecHitCollectionMiniAOD")
  , mvaPasses_             (nEleMaps_)
  , mvaValues_             (nValMaps_)
  , mvaCats_               (nCats_)
  , variableHelper_        (consumesCollector())
  , mvaVarMngr_            (iConfig.getParameter<std::string>("variableDefinition"))
  , nVars_                 (mvaVarMngr_.getNVars())
  , vars_                  (nVars_)
  , doEnergyMatrix_        (iConfig.getParameter<bool>("doEnergyMatrix"))
  , energyMatrixSize_      (iConfig.getParameter<int>("energyMatrixSize"))
  {
  
    genTauJetCollection_ = consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("genTauJetCollection"));

  // eleMaps
    for (auto const& tag : eleMapTags_) {
        eleMapTokens_.push_back(consumes<edm::ValueMap<bool> >(edm::InputTag(tag)));
    }
    // valMaps
    for (auto const& tag : valMapTags_) {
        valMapTokens_.push_back(consumes<edm::ValueMap<float> >(edm::InputTag(tag)));
    }
    // categories
    for (auto const& tag : mvaCatTags_) {
        mvaCatTokens_.push_back(consumes<edm::ValueMap<int> >(edm::InputTag(tag)));
    }

   // Book tree
   usesResource(TFileService::kSharedResource);
   edm::Service<TFileService> fs ;
   tree_  = fs->make<TTree>("tree","tree");

   tree_->Branch("nEvent",  &nEvent_);
   tree_->Branch("nRun",    &nRun_);
   tree_->Branch("nLumi",   &nLumi_);
   if (isMC_) tree_->Branch("genNpu", &genNpu_);
   tree_->Branch("vtxN",   &vtxN_);

   tree_->Branch("ele_q",&eleQ_);
   tree_->Branch("ele_3q",&ele3Q_);
   
   //PF vars
   tree_->Branch("ele_IsMvaIsolated",&eleIsMvaIsolated_);
   tree_->Branch("ele_IsMvaNonIsolated",&eleIsMvaNonIsolated_);
   tree_->Branch("passElectronSelection",&passElectronSelection_);
   // passElectronSelection

   if (doEnergyMatrix_) tree_->Branch("energyMatrix",&energyMatrix_);

   if (isMC_) tree_->Branch("matchedToGenEle",   &matchedToGenEle_);
   if (isMC_) tree_->Branch("mclassEle", &mclassEle_);
   if (isMC_) tree_->Branch("matchedToGenPion",   &matchedToGenPion_);
   if (isMC_) tree_->Branch("matchedToGenPhoton",   &matchedToGenPhoton_);
   if (isMC_) tree_->Branch("matchedToGenNeuPion",   &matchedToGenNeuPion_);
   if (isMC_) tree_->Branch("matchedToHadron",   &matchedToHadron_);
   if (isMC_) tree_->Branch("matchedToGenTauJet",   &matchedToGenTauJet_);

   for (int i = 0; i < nVars_; ++i) tree_->Branch(mvaVarMngr_.getName(i).c_str(), &vars_[i]);

   tree_->Branch("ele_isEB",&eleIsEB_);
   tree_->Branch("ele_isEE",&eleIsEE_);
   tree_->Branch("ele_isEBEtaGap",&eleIsEBEtaGap_);
   tree_->Branch("ele_isEBPhiGap",&eleIsEBPhiGap_);
   tree_->Branch("ele_isEBEEGap", &eleIsEBEEGap_);
   tree_->Branch("ele_isEEDeeGap",&eleIsEEDeeGap_);
   tree_->Branch("ele_isEERingGap",&eleIsEERingGap_);

   tree_->Branch("ele_index",&eleIndex_);

   // IDs
   for (size_t k = 0; k < nValMaps_; ++k) {
       tree_->Branch(valMapBranchNames_[k].c_str() ,  &mvaValues_[k]);
   }

   for (size_t k = 0; k < nEleMaps_; ++k) {
       tree_->Branch(eleMapBranchNames_[k].c_str() ,  &mvaPasses_[k]);
   }

   for (size_t k = 0; k < nCats_; ++k) {
       tree_->Branch(mvaCatBranchNames_[k].c_str() ,  &mvaCats_[k]);
   }
}


// ------------ method called for each event  ------------
void
ElectronMVANtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    // Fill global event info
    nEvent_ = iEvent.id().event();
    nRun_   = iEvent.id().run();
    nLumi_  = iEvent.luminosityBlock();

    // Get Handles
    auto src          = src_.getValidHandle(iEvent);
    auto vertices     = vertices_.getValidHandle(iEvent);

    // initialize cluster tools
    std::unique_ptr<noZS::EcalClusterLazyTools> lazyTools;
    if(doEnergyMatrix_) {
        // Configure Lazy Tools, which will compute 5x5 quantities
        lazyTools = std::make_unique<noZS::EcalClusterLazyTools>(
                iEvent, iSetup, ebRecHits_.get(iEvent), eeRecHits_.get(iEvent));
    }

    // Get MC only Handles, which are allowed to be non-valid
    auto genParticles = genParticles_.getHandle(iEvent);
    //auto packedGenParticles = packedGenParticles_.getHandle(iEvent);
    auto pileup       = pileup_.getHandle(iEvent);

    vtxN_ = vertices->size();

    // Fill with true number of pileup
    if(isMC_) {
       for(const auto& pu : *pileup)
       {
           int bx = pu.getBunchCrossing();
           if(bx == 0)
           {
               genNpu_ = pu.getPU_NumInteractions();
               break;
           }
       }


    }///if(isMC_) 

    // Get MVA decisions
    edm::Handle<edm::ValueMap<bool> > decisions[nEleMaps_];
    for (size_t k = 0; k < nEleMaps_; ++k) {
        iEvent.getByToken(eleMapTokens_[k],decisions[k]);
    }

    // Get MVA values
    edm::Handle<edm::ValueMap<float> > values[nValMaps_];
    for (size_t k = 0; k < nValMaps_; ++k) {
        iEvent.getByToken(valMapTokens_[k],values[k]);
    }

    // Get MVA categories
    edm::Handle<edm::ValueMap<int> > mvaCats[nCats_];
    for (size_t k = 0; k < nCats_; ++k) {
        iEvent.getByToken(mvaCatTokens_[k],mvaCats[k]);
    }

    ///gen tau jet
    typedef edm::View<reco::Candidate> refCandidateCollection;
    edm::Handle<refCandidateCollection> ReferenceCollection;
    if(isMC_){
      bool isRef = iEvent.getByToken(genTauJetCollection_, ReferenceCollection);
      if (!isRef) {
	edm::LogWarning("ElectronMVANtuplizer") << "Tau gen jetcollection not found  ";
      }
    }///if(isMC_)

    eleIndex_ = src->size();
    for(auto const& ele : src->ptrs())
    {
        if (ele->pt() < ptThreshold_) continue;

        // Fill the energy matrix around the seed
        if(doEnergyMatrix_) {
            const auto& seed = *(ele->superCluster()->seed());
            energyMatrix_ = lazyTools->energyMatrix(seed, energyMatrixSize_);
        }

        // Fill various tree variable
        eleQ_ = ele->charge();
        ele3Q_ = ele->chargeInfo().isGsfCtfScPixConsistent;

	eleIsMvaIsolated_ = ele->mva_Isolated();
	eleIsMvaNonIsolated_ = ele->mva_e_pi();
	passElectronSelection_ = passElectronSel( *ele);

        for (int iVar = 0; iVar < nVars_; ++iVar) {
            std::vector<float> extraVariables = variableHelper_.getAuxVariables(ele, iEvent);
            vars_[iVar] = mvaVarMngr_.getValue(iVar, *ele, extraVariables);
        }

        if (isMC_) {
	    //std::cout<<"particle.pdgId : "<<std::endl;
            mclassEle_ = MultiClass( *ele);
            matchedToGenEle_ = matchToTruth( *ele, *genParticles);
            matchedToGenPion_ = matchToPion( *ele, *genParticles);
	    matchedToGenPhoton_ = matchToPhoton( *ele, *genParticles);
	    matchedToGenNeuPion_ = matchToNeuPion( *ele, *genParticles);
	    matchedToHadron_ = matchToHadron( *ele, *genParticles);

	    ////check if matched to genTauJet
	    matchedToGenTauJet_ = matchToGenTauJets( *ele, *ReferenceCollection);
	    
        }

        // gap variables
        eleIsEB_ = ele->isEB();
        eleIsEE_ = ele->isEE();
        eleIsEBEEGap_ = ele->isEBEEGap();
        eleIsEBEtaGap_ = ele->isEBEtaGap();
        eleIsEBPhiGap_ = ele->isEBPhiGap();
        eleIsEEDeeGap_ = ele->isEEDeeGap();
        eleIsEERingGap_ = ele->isEERingGap();

        //
        // Look up and save the ID decisions
        //
        for (size_t k = 0; k < nEleMaps_; ++k) mvaPasses_[k] = static_cast<int>((*decisions[k])[ele]);
        for (size_t k = 0; k < nValMaps_; ++k) mvaValues_[k] = (*values[k])[ele];
        for (size_t k = 0; k < nCats_   ; ++k) mvaCats_[k]   = (*mvaCats[k])[ele];
	
        tree_->Fill();
    }

}


float ElectronMVANtuplizer::MultiClass(reco::GsfElectron const& electron)
{
    std::cout<<"Line1\n";
    tensorflow::setLogging("2");
    std::cout<<"Line2\n";
    // load the graph definition
    tensorflow::GraphDef* graphDef = tensorflow::loadGraphDef("/afs/cern.ch/user/a/akapoor/workspace/2020/EGamma_ggAnalysis_Ntuplizer/new/CMSSW_10_6_3/src/RecoEgamma/ElectronIdentification/data/DNN_rechitandclusteriso_2drwt_withpteta_modelDNN.pb");
    // create a session
    std::cout<<"Line3\n";
    tensorflow::Session* session = tensorflow::createSession(graphDef);
    std::cout<<"Line4\n";
    tensorflow::Tensor input(tensorflow::DT_FLOAT, { 1, 24 });
    std::cout<<"Line5\n";
    for (size_t i = 0; i < 24; i++) {
	input.matrix<float>()(0, i) = float(i);
    }
    std::cout<<"Line6\n";
    std::vector<tensorflow::Tensor> outputs;
    //x1 = tf.placeholder(tf.float32, shape=(None, None, None, None))
    //outputs[0].matrix<float>()(0, 0)=float(0);
    //outputs[0].matrix<float>()(0, 1)=float(1);
    //outputs[0].matrix<float>()(0, 2)=float(2);
    //outputs[0].matrix<float>()(0, 3)=float(3);
    //outputs[0].matrix<float>()(0, 4)=float(4);
    std::cout<<"Line7\n";
    tensorflow::run(session, { { "input", input } }, { "output" }, &outputs);
    std::cout<<"Line8\n";
    // process the output tensor
    // (example: print the 5th value of the 0th (the only) example)
    std::cout << outputs[0].matrix<float>()(0, 4) << std::endl;
    // -> float
    std::cout<<"Line9\n";
    tensorflow::closeSession(session);
    delete graphDef;
    std::cout<<"Line10\n";
    return outputs[0].matrix<float>()(0, 4);
    std::cout<<"Line11\n";
}

int ElectronMVANtuplizer::matchToTruth(reco::GsfElectron const& electron,
                                       edm::View<reco::GenParticle> const& genParticles) const
{
  //
  // Explicit loop and geometric matching method (advised by Josh Bendavid)
  //

  // Find the closest status 1 gen electron to the reco electron
  double dR = 999;
  reco::GenParticle const* closestElectron = nullptr;
  for(auto const& particle : genParticles) {
      //std::cout<<"particle.pdgId : "<<particle.pdgId()<<std::endl;
    // Drop everything that is not electron or not status 1
    if( std::abs(particle.pdgId()) != 11 || particle.status() != 1 )
      continue;
    //
    double dRtmp = ROOT::Math::VectorUtil::DeltaR( electron.p4(), particle.p4() );
    if( dRtmp < dR ){
      dR = dRtmp;
      closestElectron = &particle;
    }
  }
  // See if the closest electron is close enough. If not, no match found.
  if( closestElectron == nullptr || dR >= deltaR_ ) return UNMATCHED;

  if( closestElectron->isPromptFinalState() ) return TRUE_PROMPT_ELECTRON;

  if( closestElectron->isDirectPromptTauDecayProductFinalState() ) return TRUE_ELECTRON_FROM_TAU;

  //if( closestElectron->isDirectHadronDecayProduct()) return TRUE_ELECTRON_FROMHADRONDECAY;
  
  // What remains is true non-prompt electrons
  return TRUE_NON_PROMPT_ELECTRON;
}


int ElectronMVANtuplizer::matchToHadron(reco::GsfElectron const& electron,
                                       edm::View<reco::GenParticle> const& genParticles) const
{
  //
  // Explicit loop and geometric matching method (advised by Josh Bendavid)
  //

  // Find the closest status 1 gen electron to the reco electron
  double dR = 999;
  reco::GenParticle const* closestElectron = nullptr;
  for(auto const& particle : genParticles) {
      //std::cout<<"particle.pdgId : "<<particle.pdgId()<<std::endl;
    // Drop everything that is not electron or not status 1
      if( std::abs(particle.pdgId()) != 11 || particle.status() != 1 )
      continue;
    //
    double dRtmp = ROOT::Math::VectorUtil::DeltaR( electron.p4(), particle.p4() );
    if( dRtmp < dR ){
      dR = dRtmp;
      closestElectron = &particle;
    }
  }
  // See if the closest electron is close enough. If not, no match found.
  if( closestElectron == nullptr || dR >= deltaR_ ) return H_UNMATCHED;

  if( closestElectron->isPromptFinalState() ) return H_TRUE_PROMPT_ELECTRON;

  if( closestElectron->isDirectPromptTauDecayProductFinalState() ) return H_TRUE_ELECTRON_FROM_TAU;

  if( closestElectron->statusFlags().isDirectHadronDecayProduct()) return H_TRUE_ELECTRON_FROMHADRONDECAY;
  
  // What remains is true non-prompt electrons
  return H_TRUE_NON_PROMPT_ELECTRON;
}

int ElectronMVANtuplizer::matchToPion(reco::GsfElectron const& electron,
                                       edm::View<reco::GenParticle> const& genParticles) const
{
  //
  // Explicit loop and geometric matching method (advised by Josh Bendavid)
  //

  // Find the closest status 1 gen electron to the reco electron
  double dR = 999;
  reco::GenParticle const* closestPion = nullptr;
  for(auto const& particle : genParticles) {
    // Drop everything that is not pion or not status 1
      if( std::abs(particle.pdgId()) != 211 || particle.status() != 1)	 
	continue;
    double dRtmp = ROOT::Math::VectorUtil::DeltaR( electron.p4(), particle.p4() );
    if( dRtmp < dR ){
      dR = dRtmp;
      closestPion = &particle;
      // if(dR<0.1){
    // 	  std::cout<<"Found PionMatch"<<std::endl;      
    // 	  std::cout<<"closestPion->pdgId : "<<closestPion->pdgId()<<std::endl;
    // 	  std::cout<<"closestPion->pt : "<<closestPion->pt()<<std::endl;
    // 	  std::cout<<"electron pt : "<<electron.pt()<<std::endl;
    // 	  std::cout<<"closestPion dR : "<<dR<<std::endl;}
    }
  }
  // See if the closest electron is close enough. If not, no match found.
  if( closestPion == nullptr ) return P_UNMATCHED;
  if( dR >= deltaR_ ) return P_FAR;

  if( closestPion->isPromptFinalState() ) return P_TRUE_PROMPT_ELECTRON;

  if( closestPion->isDirectPromptTauDecayProductFinalState() ) return P_TRUE_ELECTRON_FROM_TAU;

  if( closestPion->statusFlags().isDirectHadronDecayProduct()) return P_TRUE_ELECTRON_FROMHADRONDECAY;
  // What remains is true non-prompt electrons
  return P_TRUE_NON_PROMPT_ELECTRON;
  }



int ElectronMVANtuplizer::matchToNeuPion(reco::GsfElectron const& electron,
					 edm::View<reco::GenParticle> const& genParticles) const
{
    //
    // Explicit loop and geometric matching method (advised by Josh Bendavid)
    //

    // Find the closest status 1 gen electron to the reco electron
    double dR = 999;
    reco::GenParticle const* closestPion = nullptr;
    for(auto const& particle : genParticles) {
	// Drop everything that is not pion or not status 1
	if(std::abs(particle.pdgId()) != 111 || particle.status() != 1) 
	    continue;
	double dRtmp = ROOT::Math::VectorUtil::DeltaR( electron.p4(), particle.p4() );
	if( dRtmp < dR ){
	    dR = dRtmp;
	    closestPion = &particle;
	//     if(dR<0.1){
	// 	std::cout<<"Found PionMatch"<<std::endl;      
	// 	std::cout<<"closestPion->pdgId : "<<closestPion->pdgId()<<std::endl;
	// 	std::cout<<"closestPion->pt : "<<closestPion->pt()<<std::endl;
	// 	std::cout<<"electron pt : "<<electron.pt()<<std::endl;
	// 	std::cout<<"closestPion dR : "<<dR<<std::endl;}
	}
    }
    // See if the closest electron is close enough. If not, no match found.
    if( closestPion == nullptr ) return NP_UNMATCHED;
    if( dR >= deltaR_ ) return NP_FAR;

    if( closestPion->isPromptFinalState() ) return NP_TRUE_PROMPT_ELECTRON;

    if( closestPion->isDirectPromptTauDecayProductFinalState() ) return NP_TRUE_ELECTRON_FROM_TAU;

    if( closestPion->statusFlags().isDirectHadronDecayProduct()) return NP_TRUE_ELECTRON_FROMHADRONDECAY;
    // What remains is true non-prompt electrons
    return NP_TRUE_NON_PROMPT_ELECTRON;
}


int ElectronMVANtuplizer::matchToPhoton(reco::GsfElectron const& electron,
                                       edm::View<reco::GenParticle> const& genParticles) const
{
  //
  // Explicit loop and geometric matching method (advised by Josh Bendavid)
  //

  // Find the closest status 1 gen electron to the reco electron
  double dR = 999;
  for(auto const& particle : genParticles) {
      // Drop everything that is not pion or not status 1
      if(std::abs(particle.pdgId()) != 22 || particle.status()!=1)	 
	  continue;
      double dRtmp = ROOT::Math::VectorUtil::DeltaR( electron.p4(), particle.p4());
      if((std::abs(particle.mother()->pdgId())<=22 || particle.mother()->pdgId()==2212) && dRtmp < 0.15){
	  for(auto const& particle2 : genParticles) {
	      if(ROOT::Math::VectorUtil::DeltaR( particle.p4(), particle2.p4())>0.4 &&  particle2.status()==23){
		  if((std::abs(particle2.pdgId())<=6 && std::abs(particle2.pdgId())>=1) || std::abs(particle2.pdgId())==21){
		      //std::cout<<"closestPhoton dR : "<<dRtmp<<std::endl;
		      return 1;}}
	  }
      }
  }
  // See if the closest electron is close enough. If not, no match found.
  // What remains is true non-prompt electrons
  return 0;
}


/////Matched to Gen tau jets
//SJ:taken from https://cmssdt.cern.ch/lxr/source/Validation/RecoTau/src/TauValidationMiniAOD.cc
int ElectronMVANtuplizer::matchToGenTauJets(reco::GsfElectron const& electron,
					    edm::View<reco::Candidate>const&  genTauJet) const
{

  float dRmin = 0.15;
  int foundMatch = 0;
  typedef edm::View<reco::Candidate> refCandidateCollection; 
  for(auto const& RefJet : genTauJet) {
    float dR = deltaR(electron.eta(), electron.phi(), RefJet.eta(), RefJet.phi());
    if (dR < dRmin) {
      dRmin = dR;
    }
  }///for loop over gen tau jets
  
  if (dRmin < 0.15)
    foundMatch = 1;
  

  return foundMatch;
}


//Copied over by AK from https://cmssdt.cern.ch/lxr/source/RecoParticleFlow/PFProducer/src/PFEGammaFilters.cc?v=CMSSW_10_2_21
bool ElectronMVANtuplizer::passElectronSel(reco::GsfElectron const& electron)
{
    bool badHcal_eleEnable_ = false;
    float ele_iso_pt_ = 10.0;
    float ele_noniso_mva_ = -0.1;
    bool validHoverE = electron.hcalOverEcalValid();
    bool passEleSelection = false;
    float electronPt = electron.pt();
    if( electronPt > ele_iso_pt_) { 
	double isoDr03 = electron.dr03TkSumPt() + electron.dr03EcalRecHitSumEt() + electron.dr03HcalTowerSumEt();
	double eleEta = fabs(electron.eta());
	float ele_iso_mva_eb_ = -0.1875;
	float ele_iso_mva_ee_ = -0.1075;
	if (eleEta <= 1.485 && isoDr03 < 10.0) {
	    if( electron.mva_Isolated() > ele_iso_mva_eb_ ) 
		passEleSelection = true;
	}
	else if (eleEta > 1.485  && isoDr03 < 10.0) {
	    if( electron.mva_Isolated() > ele_iso_mva_ee_ ) 
		passEleSelection = true;
	}
    } 
   
    if(electron.mva_e_pi() > ele_noniso_mva_) {
	if (validHoverE || !badHcal_eleEnable_) {
	    passEleSelection = true; 
	} 
	else {
	    bool EE = (std::abs(electron.eta()) > 1.485); // for prefer consistency with above than with E/gamma for now
	    float badHcal_full5x5_sigmaIetaIeta_[]={0.0106, 0.0387};
	    float badHcal_eInvPInv_[]={0.184, 0.0721};
	    float badHcal_dEta_[]={0.0032*2, 0.00632*2};
	    float badHcal_dPhi_[]={0.0547, 0.0394};
	    if ((electron.full5x5_sigmaIetaIeta() < badHcal_full5x5_sigmaIetaIeta_[EE]) &&
		(std::abs(1.0-electron.eSuperClusterOverP())/electron.ecalEnergy()  < badHcal_eInvPInv_[EE]) && 
		(std::abs(electron.deltaEtaSeedClusterTrackAtVtx())  < badHcal_dEta_[EE]) && // looser in case of misalignment
		(std::abs(electron.deltaPhiSuperClusterTrackAtVtx())  < badHcal_dPhi_[EE]))
	    {
		passEleSelection = true; 
	    }
	}
    }   
    return passEleSelection;
}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ElectronMVANtuplizer::fillDescriptions(edm::ConfigurationDescriptions& descriptions)
{
    edm::ParameterSetDescription desc;
    desc.add<edm::InputTag>("src",                 edm::InputTag("gedGsfElectrons"));
    desc.add<edm::InputTag>("vertices",            edm::InputTag("offlinePrimaryVertices"));
    desc.add<edm::InputTag>("pileup",              edm::InputTag("addPileupInfo"));
    desc.add<edm::InputTag>("genParticles",        edm::InputTag("genParticles"));
    //desc.add<edm::InputTag>("packedGenParticles",  edm::InputTag("packedGenParticles"));
    desc.add<edm::InputTag>("srcMiniAOD",          edm::InputTag("slimmedElectrons"));
    desc.add<edm::InputTag>("verticesMiniAOD",     edm::InputTag("offlineSlimmedPrimaryVertices"));
    desc.add<edm::InputTag>("pileupMiniAOD",       edm::InputTag("slimmedAddPileupInfo"));
    desc.add<edm::InputTag>("genParticlesMiniAOD", edm::InputTag("prunedGenParticles"));
    desc.add<edm::InputTag>("ebReducedRecHitCollection",        edm::InputTag("reducedEcalRecHitsEB"));
    desc.add<edm::InputTag>("eeReducedRecHitCollection",        edm::InputTag("reducedEcalRecHitsEE"));
    desc.add<edm::InputTag>("ebReducedRecHitCollectionMiniAOD", edm::InputTag("reducedEgamma","reducedEBRecHits"));
    desc.add<edm::InputTag>("eeReducedRecHitCollectionMiniAOD", edm::InputTag("reducedEgamma","reducedEERecHits"));
    desc.add<std::string>("variableDefinition");
    desc.add<bool>("doEnergyMatrix", false);
    desc.add<int>("energyMatrixSize", 2)->setComment("extension of crystals in each direction away from the seed");
    desc.add<bool>("isMC", true);
    desc.add<double>("deltaR", 0.1);
    desc.add<double>("ptThreshold", 5.0);
    desc.add<edm::InputTag>("genTauJetCollection",        edm::InputTag("tauGenJets")); 
    desc.add<std::vector<std::string>>("eleMVAs", {});
    desc.add<std::vector<std::string>>("eleMVALabels", {});
    desc.add<std::vector<std::string>>("eleMVAValMaps", {});
    desc.add<std::vector<std::string>>("eleMVAValMapLabels", {});
    desc.add<std::vector<std::string>>("eleMVACats", {});
    desc.add<std::vector<std::string>>("eleMVACatLabels", {});
    descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(ElectronMVANtuplizer);
