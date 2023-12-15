#----------------------------------------------------

PROGRAM = RDFfunc

HDRS = 	basic_sel.h \
		GetPFTrk.h

OBJS = basic_sel.o GetPFTrk.o\
	dict_$(PROGRAM).o


#-------------------------------------------------------
ObjSuf = o
SrcSuf = cpp
ExeSuf = exe
DllSuf = so
OutPutOpt = -o

ROOTCFLAGS = $(shell root-config --cflags)
ROOTLIBS = $(shell root-config --libs)
ROOTGLIBS = $(shell root-config --glibs)

#Directories
HEADRDIR = .

#deubg option: -g
#no exceptions:  -fno-exceptions

CXX = g++
CXXFLAGS = -O3 -Wall -fPIC -g -std=c++11
LD = g++
LDFLAGS = -O3 -Wall -g
SOFLAGS = -shared
ARCHFLAGS = 

#
CXXFLAGS += $(ROOTCFLAGS) -I$(HEADRDIR)
LIBS = $(ROOTLIBS)
GLIBS = $(ROOTGLIBS)

%/%.o: %.cpp
	$(CXX) -c $(CXXFLAGS) $*.cpp

$(PROGRAM).so: $(OBJS)
	@echo "Linking $(PROGRAM).so ..."
	$(LD) $(ARCHFLAGS) $(LDFLAGS) $(SOFLAGS) $(OBJS) $(ROOTLIBS) -o$(PROGRAM).so

dict_$(PROGRAM).cpp: $(HDRS)
	@echo "Generating dictionary ..."
	rootcint -f dict_$(PROGRAM).cpp -c -p -I$(HEADRDIR) $(HDRS) Linkdef.h

clean:
	@rm -f $(OBJS) $(PROGRAM).so dict_*

#------------------------------------------------------------------------------------------