FC = gfortran
FFLAGS = -fopenmp -O0 -g

APPL = pi1.exe pi2.exe pi3.exe pi4.exe pi5.exe

all: $(APPL)

%.exe: %.o
	$(FC) $(FFLAGS) -o $@ $<

%.o: %.f90
	$(FC) $(FFLAGS) -c -o $@ $<

clean:
	$(RM) *.o *.mod $(APPL)
	$(RM) core core.*
