#include<stdio.h>
#include<math.h>
#define TOTAL 500

int main(){

	int sum = 0;

	int arr[TOTAL]={0.052072706576120995 ,
0.03301868228617428 ,
0.07099534750130346 ,
0.10072346155361855 ,
0.041020775916497866 ,
0.06031470994527472 ,
0.041528339656329565 ,
0.03302744798308622 ,
0.0519105464606167 ,
0.03359118572141416 ,
0.04325973280979906 ,
0.040770583835051506 ,
0.03302099360983293 ,
0.03394290220603584 ,
0.03438161286199858 ,
0.041717515507285106 ,
0.05787839441038731 ,
0.05800021806746251 ,
0.04119947217721191 ,
0.0673284814201819 ,
0.07428646040272188 ,
0.058074979832701996 ,
0.06684403759447838 ,
0.03399659763085906 ,
0.05966627642880361 ,
0.025310466005213854 ,
0.06784545133825048 ,
0.05321638232300417 ,
0.026000112912543435 ,
0.058779050926964546 ,
0.03321387010654547 ,
0.042028236385238955 ,
0.057510363463352906 ,
0.0582509186075795 ,
0.03334344749667014 ,
0.049268733509586764 ,
0.07395876006286302 ,
0.11537570333091961 ,
0.05852772711835117 ,
0.024454795262642243 ,
0.08476586377110937 ,
0.04197125634999921 ,
0.041964564229655846 ,
0.024844097813442052 ,
0.03244434012995113 ,
0.041524824973478106 ,
0.05860680126991147 ,
0.025154521507111158 ,
0.05267037644774486 ,
0.04364836518903153 ,
0.034220183691669646 ,
0.0246870315655018 ,
0.04186699058616731 ,
0.06792524397824268 ,
0.05015338151430482 ,
0.03281460191410475 ,
0.044000184239933106 ,
0.1399740329218247 ,
0.025201243975376566 ,
0.033082547735251176 ,
0.04131372946809994 ,
0.033618132813615045 ,
0.03300557247862919 ,
0.06620821931019671 ,
0.04258535772007235 ,
0.024813302063318436 ,
0.03292107813126664 ,
0.03481984374085545 ,
0.03497305912699054 ,
0.06593837547810774 ,
0.06670283124994159 ,
0.03400017105913487 ,
0.11572829819118023 ,
0.07360165843366384 ,
0.06563526758055263 ,
0.08281489332963735 ,
0.024829849646187695 ,
0.05910796192274721 ,
0.0345037213268308 ,
0.04210649630284415 ,
0.06739299794691317 ,
0.04180634465296647 ,
0.05011375393758603 ,
0.05713328516111852 ,
0.05765997384716865 ,
0.041838462713377565 ,
0.09055897995620908 ,
0.04330092092297132 ,
0.06488237359085254 ,
0.03401297425311487 ,
0.04270467029837441 ,
0.04956637204705422 ,
0.04962644684906439 ,
0.06774757998054455 ,
0.12806684296594154 ,
0.04309033895235283 ,
0.0504821020134052 ,
0.0344919180599576 ,
0.054000202035718876 ,
0.042155131158748964 ,
0.058127156201218916 ,
0.024875456741033804 ,
0.026000111548427136 ,
0.04294490212664424 ,
0.041944712702473186 ,
0.025011159717398 ,
0.04215494016846809 ,
0.025169572354688672 ,
0.04307188584314073 ,
0.05213309853527476 ,
0.03313419022952242 ,
0.05099304280171467 ,
0.04992819586517934 ,
0.04260497346646895 ,
0.05742698867398571 ,
0.05076276172477303 ,
0.041560466802629 ,
0.05029508300497708 ,
0.03462429535748874 ,
0.07598791667331806 ,
0.06688673100920209 ,
0.03483893614196393 ,
0.03368859264666693 ,
0.10007524205620069 ,
0.07405599169521604 ,
0.02600010811273587 ,
0.05835940475972081 ,
0.057273254073611335 ,
0.025208842442907175 ,
0.041084926446119385 ,
0.04980746202763833 ,
0.0671532339680917 ,
0.06496713594983934 ,
0.04135276445160234 ,
0.041316988097567287 ,
0.050128734490229185 ,
0.06800022821344369 ,
0.08255349871511239 ,
0.07781686276020552 ,
0.05747065954262663 ,
0.07667166703131455 ,
0.148905352589602 ,
0.032808152521026965 ,
0.024959016647855343 ,
0.050171996091931445 ,
0.05785564948036984 ,
0.05072665444705242 ,
0.033484903105904 ,
0.05937478147737994 ,
0.05910660911376345 ,
0.07481524824531167 ,
0.080096513435692 ,
0.03283594614835302 ,
0.03541696624099111 ,
0.05105180619122568 ,
0.03468401078957241 ,
0.049382873322549925 ,
0.0569598522950312 ,
0.041867917070050206 ,
0.07728670116909638 ,
0.03433893970400753 ,
0.051964796440445424 ,
0.034665001741049015 ,
0.032882627841174114 ,
0.083641177668301 ,
0.04368384296123347 ,
0.07520375816202607 ,
0.041373696316174366 ,
0.040547191185693734 ,
0.0347285448189196 ,
0.026000114534356463 ,
0.02494260079363636 ,
0.03338139577728938 ,
0.032822659646618874 ,
0.05768341900015351 ,
0.02600011082013349 ,
0.06696232831792971 ,
0.05173644929242575 ,
0.043926177344034506 ,
0.034474979778428956 ,
0.0972945179400291 ,
0.05034034255675723 ,
0.024853601888037997 ,
0.025090688141522426 ,
0.05013407618303425 ,
0.06497485289995239 ,
0.04149510270183278 ,
0.04104668618313796 ,
0.042609142616910345 ,
0.09453508512909517 ,
0.032751504788617825 ,
0.03257808837203564 ,
0.04969681626589663 ,
0.03400013408650977 ,
0.06619635861271142 ,
0.0423415974689276 ,
0.033690900517919634 ,
0.050121158118651504 ,
0.058045016420502825 ,
0.049620500734899806 ,
0.025075670679939682 ,
0.0940956817880167 ,
0.03440229674202726 ,
0.04227111056043458 ,
0.05942954205776032 ,
0.03364636989756019 ,
0.04158562706325581 ,
0.0889722688830356 ,
0.03281506669962078 ,
0.04059741962442674 ,
0.04238233545063324 ,
0.058539569194303705 ,
0.042070981115411105 ,
0.03260574501220587 ,
0.042540290992219766 ,
0.07627863221906311 ,
0.03412026141361126 ,
0.05212799919572236 ,
0.03290662187414594 ,
0.02483393560557423 ,
0.03497613019043885 ,
0.04988253748944907 ,
0.058238582463577146 ,
0.040539277855573666 ,
0.07852734806395817 ,
0.03531665445771406 ,
0.04187694720003046 ,
0.032983560194296775 ,
0.06539814293928563 ,
0.06662374194337778 ,
0.07789392221107451 ,
0.0260001267042855 ,
0.06611706238140379 ,
0.1010511167159199 ,
0.024617221424481448 ,
0.05211607088252664 ,
0.02522646767413264 ,
0.033337555835775724 ,
0.03296753244883125 ,
0.045407428743814864 ,
0.03346452413115375 ,
0.04360293737616098 ,
0.04078532535565744 ,
0.050811519050595985 ,
0.05853112263407635 ,
0.03333177966932934 ,
0.0848658092205194 ,
0.04335662431931156 ,
0.0659285498653599 ,
0.049282555458780665 ,
0.025120745571882604 ,
0.049932520879721984 ,
0.024862411074460168 ,
0.02600012836697132 ,
0.04956259790474547 ,
0.041863463903052 ,
0.06166113639924182 ,
0.041566914151699705 ,
0.032925741185755496 ,
0.0328485243479849 ,
0.04943838984371509 ,
0.08279102269285878 ,
0.05057399062007339 ,
0.06609899115646037 ,
0.0525154781563016 ,
0.09473138742143118 ,
0.051079867037836395 ,
0.05181471664471138 ,
0.08472760835673505 ,
0.034999377862939204 ,
0.025882897705234695 ,
0.034525308067105444 ,
0.08450962907624125 ,
0.02600013735463086 ,
0.024785890100293192 ,
0.07868107407900271 ,
0.04205767018528059 ,
0.04250493225848505 ,
0.03400013699434385 ,
0.02600013087494365 ,
0.05026012837846936 ,
0.04195590483211581 ,
0.034127089548587536 ,
0.04502294772607521 ,
0.04194494131367089 ,
0.024612708324330698 ,
0.025392505402258174 ,
0.041774575739815675 ,
0.07379841977836113 ,
0.06897005120076949 ,
0.04299671975776696 ,
0.0501045454179209 ,
0.042420887943593985 ,
0.05001229719654129 ,
0.02479795837598747 ,
0.06730793746908938 ,
0.04198652603922204 ,
0.05073214564584175 ,
0.09104294458312714 ,
0.033391734067504814 ,
0.090789429110302 ,
0.05909228104060497 ,
0.05862891848849634 ,
0.025142522252202874 ,
0.04321720422869762 ,
0.05886083292751588 ,
0.050727473705318396 ,
0.042713010193290504 ,
0.04161344283836004 ,
0.05051475989050999 ,
0.03472383114983425 ,
0.06098388648830258 ,
0.03463753946280581 ,
0.05102247390020853 ,
0.024772080974450356 ,
0.06519444288929271 ,
0.04225980702724231 ,
0.041947941379053055 ,
0.05156508371228906 ,
0.024996798862701133 ,
0.04372377679403089 ,
0.04280325375379043 ,
0.06555357293000127 ,
0.050429653315018357 ,
0.033307846101851814 ,
0.08390193491738843 ,
0.05205471561881863 ,
0.033931422815842854 ,
0.041539839041073376 ,
0.040741222012008985 ,
0.074788704059329 ,
0.025252278360762933 ,
0.03293974995494082 ,
0.12267551515187713 ,
0.02491119314246162 ,
0.02539817899296193 ,
0.0332583139888136 ,
0.04099807722227539 ,
0.03304354856753963 ,
0.04256078543316674 ,
0.024915322807467145 ,
0.03308216951826505 ,
0.05028221654076391 ,
0.025060436178137673 ,
0.050222977570746 ,
0.02541545077784635 ,
0.04225958335050538 ,
0.034350841826336145 ,
0.034528967393881865 ,
0.03329256860383015 ,
0.04289743350541621 ,
0.041362538301979335 ,
0.07617178166133724 ,
0.04091444445834491 ,
0.025112766866758056 ,
0.06698248895764786 ,
0.02464500139136335 ,
0.033474064833215994 ,
0.024877348535616656 ,
0.04157630494817739 ,
0.049290965545374175 ,
0.0754281598149141 ,
0.08295958582230219 ,
0.08213516283862866 ,
0.03410995761607566 ,
0.0412853041006192 ,
0.06839971391407003 ,
0.03368955886766194 ,
0.06155144281824115 ,
0.034000132595167626 ,
0.04121135499376364 ,
0.058418084692547834 ,
0.04094427084272448 ,
0.04064481819420619 ,
0.041293123650031786 ,
0.03439707167791423 ,
0.0341003196528735 ,
0.05892358265580626 ,
0.05005817234332627 ,
0.03277279912600314 ,
0.0342358580785705 ,
0.03458404916259066 ,
0.04198380756437392 ,
0.058162331932062515 ,
0.04191826725012973 ,
0.049899029247787614 ,
0.04171146288696172 ,
0.02453495056158821 ,
0.03286700459549324 ,
0.06701902801737504 ,
0.042966081151464906 ,
0.05961120679282426 ,
0.17791800927682572 ,
0.12450432088409537 ,
0.02497383957298031 ,
0.05674547460026542 ,
0.03419434289614223 ,
0.05115111974224809 ,
0.033883272482894834 ,
0.03272995507642502 ,
0.051779307628297556 ,
0.026000098962287915 ,
0.06007613162608287 ,
0.06713054074466221 ,
0.04247215750676646 ,
0.033483607116072386 ,
0.04156401923812085 ,
0.02479416211884592 ,
0.08540655435622513 ,
0.04905712100231534 ,
0.04110200177802408 ,
0.024960938886510797 ,
0.03329163173071993 ,
0.04084769722895267 ,
0.043342912118305134 ,
0.08503460938822371 ,
0.08402420031107855 ,
0.033952844987726175 ,
0.03350589905876834 ,
0.025120881428491972 ,
0.02568185407870275 ,
0.033898671830694484 ,
0.04184759827836966 ,
0.026136468973741278 ,
0.050740609259495084 ,
0.03346007830815506 ,
0.03268148884559198 ,
0.04217082729819338 ,
0.04227211875310055 ,
0.041128850659722764 ,
0.07066229329412485 ,
0.05783648217146288 ,
0.05811202450659285 ,
0.04187154645550802 ,
0.041050797118102396 ,
0.0433467174623123 ,
0.06124755570799558 ,
0.024816809546303983 ,
0.03308729039219968 ,
0.052544749024207735 ,
0.058241693804451516 ,
0.049456630802346746 ,
0.04944801201882936 ,
0.040642425947458 ,
0.03299370385825472 ,
0.034353822015967116 ,
0.05980012721553889 ,
0.024922972962231116 ,
0.04274826674769597 ,
0.05895962625597026 ,
0.044136279557240574 ,
0.05763578829963793 ,
0.02467480586887775 ,
0.02523704171892039 ,
0.058097800990837514 ,
0.0499453183185084 ,
0.05132685706145503 ,
0.05146044388183134 ,
0.03252217911388347 ,
0.02493346314430533 ,
0.0423428003714844 ,
0.03332204948281492 ,
0.07184252831410208 ,
0.034000158552487045 ,
0.041393105825337784 ,
0.04131288306008004 ,
0.043348511285456394 ,
0.03352838349147592 ,
0.03358023071385205 ,
0.0700937004809954 ,
0.0423019032887617 ,
0.03282368006424011 ,
0.025876595366626343 ,
0.04224496193810885 ,
0.03291512646546701 ,
0.057665046945487054 ,
0.02600013559279685 ,
0.05005851661932781 ,
0.02600010866439071 ,
0.04269293511047352 ,
0.05848465608725135 ,
0.03355442362761429 ,
0.04882169159489577 ,
0.04168323813787578 ,
0.10233927483173755 ,
0.034080117972232 ,
0.033136610416153414 ,
0.034419571579610495 ,
0.05986583320783908 ,
0.07622974935332012 ,
0.025479827547181592 ,
0.05831093526277141 ,
0.049808796885898336 ,
0.03401694535510701 ,
0.04981021653538467 ,
0.08330474811460853 ,
0.02473896487176181 ,
0.024795900249241748 ,
0.06608439571906653 ,
0.04161204951731309};

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
