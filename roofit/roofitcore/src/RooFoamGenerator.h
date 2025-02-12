/*****************************************************************************
 * Project: RooFit                                                           *
 * Package: RooFitCore                                                       *
 *    File: $Id$
 * Authors:                                                                  *
 *   WV, Wouter Verkerke, UC Santa Barbara, verkerke@slac.stanford.edu       *
 *   DK, David Kirkby,    UC Irvine,         dkirkby@uci.edu                 *
 *                                                                           *
 * Copyright (c) 2000-2005, Regents of the University of California          *
 *                          and Stanford University. All rights reserved.    *
 *                                                                           *
 * Redistribution and use in source and binary forms,                        *
 * with or without modification, are permitted according to the terms        *
 * listed in LICENSE (http://roofit.sourceforge.net/license.txt)             *
 *****************************************************************************/
#ifndef ROO_FOAM_GENERATOR
#define ROO_FOAM_GENERATOR

#include "RooAbsNumGenerator.h"
#include "RooPrintable.h"
#include "RooArgSet.h"

class RooAbsReal;
class RooRealVar;
class RooDataSet;

class TFoam ;
class RooTFoamBinding ;
class RooNumGenFactory ;

class RooFoamGenerator : public RooAbsNumGenerator {
public:
  RooFoamGenerator() = default;
  RooFoamGenerator(const RooAbsReal &func, const RooArgSet &genVars, const RooNumGenConfig& config, bool verbose=false, const RooAbsReal* maxFuncVal=nullptr);
  RooAbsNumGenerator* clone(const RooAbsReal& func, const RooArgSet& genVars, const RooArgSet& /*condVars*/,
             const RooNumGenConfig& config, bool verbose=false, const RooAbsReal* maxFuncVal=nullptr) const override {
    return new RooFoamGenerator(func,genVars,config,verbose,maxFuncVal) ;
  }
  ~RooFoamGenerator() override;

  const RooArgSet *generateEvent(UInt_t remaining, double& resampleRatio) override;

  TFoam& engine() { return *_tfoam; }

  bool canSampleConditional() const override { return false ; }
  bool canSampleCategories() const override { return false ; }

  std::string const& generatorName() const override;

protected:

  friend class RooNumGenFactory ;
  static void registerSampler(RooNumGenFactory& fact) ;

  RooTFoamBinding *_binding = nullptr; ///< Binding of RooAbsReal to TFoam function interface
  TFoam *_tfoam = nullptr;             ///< Instance of TFOAM generator
  double *_xmin = nullptr;             ///< Lower bound of observables to be generated ;
  double *_range = nullptr;            ///< Range of observables to be generated ;
  double *_vec = nullptr;              ///< Transfer array for FOAM output
};

#endif
