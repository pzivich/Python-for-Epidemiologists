**********************************************************************
* Demonstration of AIPW with a single sample
*	Data generating mechanism comes from Funk et al. (2011). See
*	online supplementary information for details (or the dgm.py file)
*
* Paul Zivich
**********************************************************************;

%let source=X:\filepath\;

/*Loading the data*/
PROC IMPORT DATAFILE="&source\dr_data.csv" OUT=dat DBMS=dlm;
	GETNAMES=YES;
	DELIMITER=',';
RUN;
PROC CONTENTS DATA=dat;
RUN;
DATA dat;
	SET dat;
	id = _N_;
RUN;

/*Estimating Propensity Score (IPW)*/
PROC GENMOD DATA=dat DESC;
	MODEL X = Z1 Z3 / DIST=b;
	OUTPUT OUT=ps P=ps;
RUN;

/*Estimating Outcome Model (g-formula)*/
DATA onesample; *SAS is annoying. So we generate 3 copies of the data internally;
	SET dat;
	LABEL interv = "Intervention";
	interv = -1;
	OUTPUT;

	interv = 0;
	X = 0;
	Y = .;
	OUTPUT;

	interv = 1;
	X = 1;
	Y = .;
	OUTPUT;
RUN;
PROC REG DATA=onesample PLOTS=NONE;
	MODEL Y = X Z1 Z3;
	OUTPUT OUT=y_pred P=y_pred;
RUN; QUIT;

DATA all_treat;
	SET y_pred;
	WHERE interv = 1;
	RENAME y_pred=y_x1;
	KEEP id y_pred;
RUN;
DATA non_treat;
	SET y_pred;
	WHERE interv = 0;
	RENAME y_pred=y_x0;
	KEEP id y_pred;
RUN;

DATA final;
	MERGE ps all_treat non_treat;
	BY id;
RUN;


/*Generating Pseudo-Outcomes*/

/*AIPW Estimates*/
DATA final;
	SET final;
	y_x1_star = (Y*X)/ps + (y_x1*(ps-X))/ps;
	y_x0_star = (Y*(1-X))/(1-ps) + (y_x0*(X-ps))/(1-ps);
	pseudo_y = y_x1_star - y_x0_star;
RUN;
PROC MEANS DATA=final MEAN;
	VAR pseudo_y;
RUN;

*G-computation;
DATA final;
	SET final;
	gcomp_i = y_x1 - y_x0;
RUN;
PROC MEANS DATA=final MEAN;
	VAR gcomp_i;
RUN;

*IPW;
DATA final;
	SET final;
	ipw_i = Y*X / ps - Y*(1-X)/(1-ps);
RUN;
PROC MEANS DATA=final MEAN;
	VAR ipw_i;
RUN;
