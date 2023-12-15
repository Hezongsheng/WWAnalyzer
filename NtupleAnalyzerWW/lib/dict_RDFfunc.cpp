// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME dict_RDFfunc
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Header files passed as explicit arguments
#include "basic_sel.h"
#include "GetPFTrk.h"

// Header files passed via #pragma extra_include

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

namespace ROOT {
   static TClass *musf_Dictionary();
   static void musf_TClassManip(TClass*);
   static void *new_musf(void *p = nullptr);
   static void *newArray_musf(Long_t size, void *p);
   static void delete_musf(void *p);
   static void deleteArray_musf(void *p);
   static void destruct_musf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::musf*)
   {
      ::musf *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::musf));
      static ::ROOT::TGenericClassInfo 
         instance("musf", "basic_sel.h", 21,
                  typeid(::musf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &musf_Dictionary, isa_proxy, 4,
                  sizeof(::musf) );
      instance.SetNew(&new_musf);
      instance.SetNewArray(&newArray_musf);
      instance.SetDelete(&delete_musf);
      instance.SetDeleteArray(&deleteArray_musf);
      instance.SetDestructor(&destruct_musf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::musf*)
   {
      return GenerateInitInstanceLocal((::musf*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::musf*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *musf_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::musf*)nullptr)->GetClass();
      musf_TClassManip(theClass);
   return theClass;
   }

   static void musf_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *Getxsw_W_Dictionary();
   static void Getxsw_W_TClassManip(TClass*);
   static void *new_Getxsw_W(void *p = nullptr);
   static void *newArray_Getxsw_W(Long_t size, void *p);
   static void delete_Getxsw_W(void *p);
   static void deleteArray_Getxsw_W(void *p);
   static void destruct_Getxsw_W(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::Getxsw_W*)
   {
      ::Getxsw_W *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::Getxsw_W));
      static ::ROOT::TGenericClassInfo 
         instance("Getxsw_W", "basic_sel.h", 29,
                  typeid(::Getxsw_W), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &Getxsw_W_Dictionary, isa_proxy, 4,
                  sizeof(::Getxsw_W) );
      instance.SetNew(&new_Getxsw_W);
      instance.SetNewArray(&newArray_Getxsw_W);
      instance.SetDelete(&delete_Getxsw_W);
      instance.SetDeleteArray(&deleteArray_Getxsw_W);
      instance.SetDestructor(&destruct_Getxsw_W);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::Getxsw_W*)
   {
      return GenerateInitInstanceLocal((::Getxsw_W*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::Getxsw_W*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *Getxsw_W_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::Getxsw_W*)nullptr)->GetClass();
      Getxsw_W_TClassManip(theClass);
   return theClass;
   }

   static void Getxsw_W_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_musf(void *p) {
      return  p ? new(p) ::musf : new ::musf;
   }
   static void *newArray_musf(Long_t nElements, void *p) {
      return p ? new(p) ::musf[nElements] : new ::musf[nElements];
   }
   // Wrapper around operator delete
   static void delete_musf(void *p) {
      delete ((::musf*)p);
   }
   static void deleteArray_musf(void *p) {
      delete [] ((::musf*)p);
   }
   static void destruct_musf(void *p) {
      typedef ::musf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::musf

namespace ROOT {
   // Wrappers around operator new
   static void *new_Getxsw_W(void *p) {
      return  p ? new(p) ::Getxsw_W : new ::Getxsw_W;
   }
   static void *newArray_Getxsw_W(Long_t nElements, void *p) {
      return p ? new(p) ::Getxsw_W[nElements] : new ::Getxsw_W[nElements];
   }
   // Wrapper around operator delete
   static void delete_Getxsw_W(void *p) {
      delete ((::Getxsw_W*)p);
   }
   static void deleteArray_Getxsw_W(void *p) {
      delete [] ((::Getxsw_W*)p);
   }
   static void destruct_Getxsw_W(void *p) {
      typedef ::Getxsw_W current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::Getxsw_W

namespace {
  void TriggerDictionaryInitialization_dict_RDFfunc_Impl() {
    static const char* headers[] = {
"basic_sel.h",
"GetPFTrk.h",
nullptr
    };
    static const char* includePaths[] = {
"/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.26.04-edd28/x86_64-centos7-gcc11-opt/include/",
"/eos/home-z/zohe/WWAnalyzer/NtupleAnalyzerWW/lib/",
nullptr
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "dict_RDFfunc dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
class __attribute__((annotate("$clingAutoload$basic_sel.h")))  musf;
class __attribute__((annotate("$clingAutoload$basic_sel.h")))  Getxsw_W;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "dict_RDFfunc dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "basic_sel.h"
#include "GetPFTrk.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"Getxsw_W", payloadCode, "@",
"musf", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("dict_RDFfunc",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_dict_RDFfunc_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_dict_RDFfunc_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_dict_RDFfunc() {
  TriggerDictionaryInitialization_dict_RDFfunc_Impl();
}
