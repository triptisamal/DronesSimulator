#include<stdio.h>
#include<math.h>
#define TOTAL 500

int main(){

	int sum = 0;

	int arr[TOTAL]={0.03267975942894422 ,
0.041715109216006366 ,
0.04188595673875866 ,
0.041601115783125656 ,
0.1392690519214524 ,
0.041202361204342834 ,
0.03383978291603287 ,
0.02495208884173571 ,
0.042958413438193226 ,
0.057673958706745965 ,
0.0333758536530695 ,
0.04151342424665249 ,
0.03439661192691745 ,
0.04101360384626859 ,
0.03274863686325599 ,
0.04404649143698662 ,
0.03406409494564248 ,
0.05176876208730715 ,
0.058628249323963974 ,
0.03300701393271288 ,
0.04157162708531796 ,
0.0637380260959275 ,
0.0420744086948772 ,
0.06664474656286479 ,
0.05806597014852883 ,
0.04960121132576048 ,
0.026000105907348334 ,
0.04949903847209473 ,
0.024724739423996365 ,
0.03422758076039034 ,
0.032871151620797255 ,
0.0332138228635355 ,
0.025123873328437886 ,
0.10241874138355704 ,
0.06756825414648432 ,
0.033036015595424115 ,
0.04866898779186146 ,
0.0801224348403808 ,
0.03298877176066769 ,
0.024872678392319398 ,
0.03400012671498638 ,
0.08992821045624567 ,
0.049449399177440956 ,
0.05793349908612107 ,
0.04299816509064058 ,
0.04971721774255987 ,
0.02510795263106678 ,
0.024707349044088264 ,
0.050957905466396704 ,
0.05270554223144311 ,
0.06760258833431443 ,
0.03354810998711402 ,
0.06215535700041571 ,
0.04161660795287531 ,
0.03464982316907611 ,
0.024951510947807502 ,
0.049589141955823764 ,
0.03292714440401608 ,
0.04925888924012181 ,
0.041815967907234144 ,
0.03289122048026551 ,
0.04354905859948371 ,
0.042691963063578406 ,
0.02547845152456661 ,
0.05065323068753239 ,
0.04970995721010219 ,
0.04149812605879039 ,
0.058484958610622195 ,
0.02483552117025247 ,
0.02496576506214384 ,
0.040992294238377525 ,
0.0407515609282537 ,
0.06597987301758744 ,
0.08868815572281709 ,
0.032422853091890746 ,
0.05204742203594995 ,
0.06650102883748114 ,
0.04122152221938865 ,
0.03379957799889187 ,
0.06566600364260963 ,
0.043440211363978624 ,
0.04179723027056367 ,
0.03279555836442634 ,
0.032730100541520916 ,
0.06667869468307544 ,
0.034000139108949515 ,
0.025059612172685864 ,
0.04099063029128078 ,
0.058088775946854077 ,
0.032950340340926615 ,
0.03288956759635929 ,
0.04188915077630587 ,
0.025127304255307695 ,
0.051955776968042953 ,
0.04988238782741239 ,
0.09363207316390856 ,
0.07522382637085412 ,
0.07457841436345831 ,
0.05914332519985588 ,
0.07521150080427522 ,
0.03324939953916231 ,
0.06889189150546444 ,
0.043301930633464505 ,
0.02496666591322324 ,
0.024456472236468862 ,
0.0662495053794271 ,
0.033187502768650255 ,
0.05131381717647131 ,
0.042937658437891824 ,
0.033892953228395306 ,
0.04968791871564147 ,
0.025438401689297764 ,
0.042235392028111766 ,
0.06058487586592237 ,
0.05092545091726433 ,
0.14007491418250162 ,
0.036000128007329296 ,
0.02535500319070135 ,
0.0623547627323424 ,
0.04400016620834418 ,
0.08598336919211569 ,
0.025005954288827896 ,
0.06814861454943193 ,
0.05143006320943899 ,
0.07674378806511072 ,
0.04191438064394528 ,
0.04209966063705652 ,
0.02600013154665389 ,
0.03394880753704842 ,
0.05797881109810686 ,
0.07456063345034758 ,
0.033512603362591445 ,
0.06647878511969973 ,
0.033481033339274366 ,
0.10323020594205445 ,
0.025310001597006117 ,
0.03304864119440376 ,
0.08723561503554432 ,
0.0335504678207896 ,
0.0658935190768531 ,
0.07439101455644981 ,
0.02486061195765097 ,
0.06669045380933283 ,
0.06720488326409746 ,
0.04232136136355595 ,
0.05915075852257597 ,
0.02600012307163018 ,
0.050833822942614196 ,
0.08302977855542473 ,
0.03387460058647895 ,
0.03360372666763024 ,
0.04983508990970883 ,
0.033302075534927755 ,
0.11213347422186305 ,
0.0672856366425811 ,
0.0580773459401749 ,
0.042853165801135455 ,
0.04999902509099179 ,
0.07533743431921286 ,
0.0585992582803044 ,
0.03521242396445344 ,
0.03382696370802006 ,
0.03266902736357699 ,
0.06738933443832584 ,
0.034343055769735835 ,
0.08357792862320929 ,
0.034082976910176345 ,
0.02600011694084628 ,
0.024766149925987937 ,
0.04251983960607791 ,
0.04286717893024927 ,
0.04307928461709992 ,
0.042152170704104236 ,
0.02528663102873919 ,
0.07373058861289447 ,
0.1022636513312758 ,
0.04147386580882757 ,
0.05856942704467183 ,
0.041155737144751556 ,
0.05885544192156103 ,
0.049491123489770215 ,
0.025176720144505404 ,
0.04362389245752181 ,
0.034460970113791706 ,
0.025262105892808227 ,
0.041922946403612465 ,
0.026000112485573004 ,
0.043645388360209744 ,
0.05153050470477137 ,
0.04960522750046404 ,
0.033246738216633855 ,
0.043400650530167395 ,
0.033324017730224594 ,
0.05007158225570373 ,
0.04231612372536675 ,
0.026000134590848798 ,
0.03348324086447704 ,
0.03435320707141797 ,
0.04355771674665722 ,
0.07586793333864987 ,
0.033059801203084424 ,
0.02486627358694998 ,
0.09196175875473352 ,
0.03326945201235197 ,
0.05031274409763196 ,
0.042454155281352865 ,
0.06950578637161027 ,
0.05056848170627229 ,
0.04186282904852774 ,
0.050678917485935907 ,
0.08286414466135787 ,
0.025108983555842193 ,
0.050412207393880554 ,
0.033727823315658684 ,
0.024994073588415384 ,
0.033913212752422046 ,
0.03272756809467545 ,
0.025115144296906478 ,
0.03509253248378907 ,
0.04271534674785288 ,
0.06697676221511728 ,
0.05974412513682236 ,
0.03401528391177789 ,
0.0347153372390414 ,
0.06002114131768642 ,
0.02494765574719598 ,
0.033241008071406994 ,
0.041800374125086734 ,
0.07485797178502802 ,
0.06606413431523261 ,
0.024847093591388876 ,
0.08292582883945188 ,
0.07684876939649156 ,
0.04881902502692703 ,
0.024586748623680012 ,
0.0950939757065681 ,
0.05841309212731158 ,
0.026000127727774755 ,
0.0501518956806735 ,
0.05854298700561734 ,
0.07548849292385837 ,
0.06634673791856012 ,
0.05198346511016572 ,
0.053608146153663466 ,
0.03425499960436756 ,
0.05067615075512825 ,
0.025065463497817332 ,
0.061488857186376256 ,
0.05815352974190454 ,
0.03425047893591606 ,
0.02484885482631071 ,
0.0324572449051518 ,
0.03370279822231535 ,
0.09183192854609958 ,
0.025330457151355193 ,
0.03297053353501225 ,
0.02524176987081654 ,
0.07561985000055178 ,
0.03270785702261802 ,
0.07450858796726108 ,
0.05786127379027245 ,
0.024494597418450607 ,
0.04985534428969347 ,
0.05025444784758823 ,
0.042000162346513 ,
0.03302846271445289 ,
0.033988866725095726 ,
0.03354473334267519 ,
0.024798017440908877 ,
0.06575834845196418 ,
0.04871261228615036 ,
0.024959400246440916 ,
0.04258593130963026 ,
0.05109568212258736 ,
0.033081328111429414 ,
0.05117690779714627 ,
0.0842380962100878 ,
0.05053188906302043 ,
0.040882769756341426 ,
0.08475194328574477 ,
0.025671922128448266 ,
0.02470091034634582 ,
0.06544889729792526 ,
0.025355951358737708 ,
0.05891525765934434 ,
0.04156928287653184 ,
0.04941734473254392 ,
0.20035111256221225 ,
0.032489155374010446 ,
0.04342735059055145 ,
0.05000018109755545 ,
0.044111940766379976 ,
0.03454965358248609 ,
0.04111119672493537 ,
0.05073570780131622 ,
0.03323152326534972 ,
0.032879354765704506 ,
0.035786392495832244 ,
0.0745238929519872 ,
0.08368582618580839 ,
0.05785187339814562 ,
0.07704759770217035 ,
0.058151853762293745 ,
0.06603373073416209 ,
0.07516766269447028 ,
0.049679677880882185 ,
0.05890354782209078 ,
0.04131242236703633 ,
0.032807826024487126 ,
0.025058960568111237 ,
0.03273252912821249 ,
0.03288793891292112 ,
0.06793794652846379 ,
0.024716630237619545 ,
0.058551841308273726 ,
0.05138946915362792 ,
0.05327852164191728 ,
0.07408135136702942 ,
0.060549561950993556 ,
0.033351758316656765 ,
0.04091947339240071 ,
0.04219460859057183 ,
0.041956375485233524 ,
0.043965823781189274 ,
0.04340304383314163 ,
0.04306221531318697 ,
0.04378325930758396 ,
0.04962190303967799 ,
0.04559630055089649 ,
0.049602122007613714 ,
0.06617762910679527 ,
0.05861252044176346 ,
0.05887594602654161 ,
0.033534134397719136 ,
0.0251117381299025 ,
0.041471712295107994 ,
0.03356952912444264 ,
0.11597390296844823 ,
0.03462320693811232 ,
0.051092065102565254 ,
0.041609536462898014 ,
0.03528576660439863 ,
0.07635556784087966 ,
0.06872835471634961 ,
0.04213183882101103 ,
0.044000199668082655 ,
0.0248338115305742 ,
0.04159714781971109 ,
0.06906757145137546 ,
0.04140495697599323 ,
0.04208922813518539 ,
0.07505162129592836 ,
0.033929716400909485 ,
0.03351667632294257 ,
0.0659492383272654 ,
0.042700110266770605 ,
0.045005561527942085 ,
0.04983385201613022 ,
0.05854928858673843 ,
0.05187185769977222 ,
0.04191389369137082 ,
0.09162532257606744 ,
0.04097023467284294 ,
0.04129672905916161 ,
0.03315915375777288 ,
0.05004406018780217 ,
0.052442301297534695 ,
0.040830461449425995 ,
0.03393046516881511 ,
0.034151139854341345 ,
0.035521980457790314 ,
0.041661635808733416 ,
0.03489088092554776 ,
0.07426597340735266 ,
0.07514717319987377 ,
0.034306816421681055 ,
0.06607738421700804 ,
0.049997929607078787 ,
0.04929242796611353 ,
0.07391886756902435 ,
0.032797905181489166 ,
0.03404715651036978 ,
0.08488457509148403 ,
0.033869747072778664 ,
0.026000117026309888 ,
0.033560448551649254 ,
0.05929924290798005 ,
0.04212814588886271 ,
0.0344074597008927 ,
0.04219348776491469 ,
0.04065548289566792 ,
0.04110813220552332 ,
0.07538236827804924 ,
0.033099233217772604 ,
0.04208480958096408 ,
0.09429808438957027 ,
0.03397475531023677 ,
0.026000111656568684 ,
0.06698110559120157 ,
0.05312239053803581 ,
0.034411547421058036 ,
0.05000942554199777 ,
0.03405088467103988 ,
0.03452433697963155 ,
0.07545756324092176 ,
0.04958446278905308 ,
0.05035056947227529 ,
0.033293309319951225 ,
0.050326677771686 ,
0.025234110305251384 ,
0.04083476341642191 ,
0.04348218132962769 ,
0.10362475674870551 ,
0.07599762045133539 ,
0.0341798835353172 ,
0.024547781835124613 ,
0.03250488761955859 ,
0.02531287379390264 ,
0.05877945123569893 ,
0.06825104964601572 ,
0.026000104923085784 ,
0.05112568096432454 ,
0.06547104079709942 ,
0.024880918988014433 ,
0.024574661854154654 ,
0.041653247273195526 ,
0.05914518337145333 ,
0.05877670431149139 ,
0.04293861389064314 ,
0.025256164148293736 ,
0.04192141608196334 ,
0.03252309648857838 ,
0.12607317734103926 ,
0.03352615384601927 ,
0.04860302964211724 ,
0.09237578847582605 ,
0.06724967750087432 ,
0.09369399247326689 ,
0.12456189161670819 ,
0.04239898722334617 ,
0.07617645438596916 ,
0.0503173964053345 ,
0.032957543052830635 ,
0.04971295835788646 ,
0.04306602979274735 ,
0.0746580486416769 ,
0.032817833176834385 ,
0.035128571619315874 ,
0.09402539773295385 ,
0.05866429933193375 ,
0.07391763735123438 ,
0.025301013086046792 ,
0.02600012755373424 ,
0.058382578227024334 ,
0.04146280853329502 ,
0.05028908317579009 ,
0.02583612949534546 ,
0.05815840593116038 ,
0.042023441894758096 ,
0.06809400143821405 ,
0.043865225917840846 ,
0.07200023938508687 ,
0.02486668403859811 ,
0.050507293862167506 ,
0.033873449777293 ,
0.06613137713343237 ,
0.034896590984178855 ,
0.042767789271818304 ,
0.08232898394831191 ,
0.041373595697719506 ,
0.024937118886831644 ,
0.03278934694825715 ,
0.05861428657585477 ,
0.0356903165255427 ,
0.07521955832893773 ,
0.07467187010022108 ,
0.04189767844528308 ,
0.04154555382677562 ,
0.026000108999284403 ,
0.04268760856790105 ,
0.07442279358328728 ,
0.04289079165861883 ,
0.0889978040094486 ,
0.07382039844072717 ,
0.0748840771780595 ,
0.05070199232595125 ,
0.06566536539458089 ,
0.06865180214815221 ,
0.051938092785871214 ,
0.03346603528820104 ,
0.06691140809996454 ,
0.033705555456049995 ,
0.043551466277168965 ,
0.03438357495069312 ,
0.042650414965172065 ,
0.03385612904235527 ,
0.041384664650793164 ,
0.03453080978084628 ,
0.05224586343557547 ,
0.04129938450946004};

for (int i=0;i<TOTAL;i++){
	sum += arr[i];
}

float mean = 0;
mean=sum/TOTAL;
printf("Average:%f\n",mean);

float summ=0;
for (int i=0;i<TOTAL;i++){
	summ += pow((arr[i]-mean),2);
}
float sd=0;
sd = sqrt(summ/TOTAL);
printf("Standard Deviation:%f\n",sd);
//https://www.indeed.com/career-advice/career-development/how-to-calculate-confidence-interval
//standard error
float se=0;
se = sd/TOTAL;


//margin of error
float margin=0;
margin = se/2;

//confidence interval or z-value 99%
//    Confidence interval (CI) = ‾X ± Z(S ÷ √n)

//In the formula, ‾X represents the sample mean, Z represents the Z-value you get from the normal standard distribution, S is the population standard deviation and n represents the sample size you're surveying.
float ci_upper = mean+2.576*(sd/sqrt(TOTAL));
float ci_lower = mean-2.576*(sd/sqrt(TOTAL));
float ci =2.576*(sd/sqrt(TOTAL));
printf("ci = (%f,%f)\n",ci_lower,ci_upper);
printf("ci=%f\n",ci);


return 0;
}
