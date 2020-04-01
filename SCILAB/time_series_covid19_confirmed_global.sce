//from https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
//filename = fullfile( 'D:\Telecharg\time_series_2019-ncov-Confirmed.csv');
//filename = fullfile( 'time_series_2019-ncov-Confirmed.csv');
filename = fullfile( '../time_series_covid19_confirmed_global.csv');

MATRIXX = csvRead ( filename,",","double" );
MATRIXXstring = csvRead ( filename,",",".","string" );


MATRIXXtrunc=MATRIXX(:,5:$);
//X=MATRIXX(1:1,:)
X=1:size(MATRIXXtrunc)(1,2);
XT=X.';
chines  = [51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 ];

france=[118];
frances=[109 110 111 112 113 114 115 116 117 118 ];
germany=[122];
italy=[139];
us=[227];
//TODO put into set unary values because Africa is iterative subjective own process
//afriques=[67,79  ,87,  414,427,428,448,449,483];
afriques=[195,202,212, 144,158,190,201,210,216,                       202,   106];
//print names....list
MATRIXXstring(afriques,1:2)

//MATRIXX(afriques,2:$) why not printed
//MATRIXX(afriques,3:$)


uks=[219 220 221 222 223 224 225  ];
//maghrebs=[15,209];
maghrebs=[218,215];
russia=[189];

india=[133];
southKorea=[145];
//regression shape 1,9 vers 3*3 :  INC3=matrix(INC,3,3) ; INC4=INC3.' trans.'

//POUB=1:9
Ychines=sum(MATRIXXtrunc(chines,:),1);
YTchines=Ychines';

Yfrance=MATRIXXtrunc(france,:);

Yfrances=sum(MATRIXXtrunc(frances,:),1);
YTfrances=Yfrances';

Ygerm=sum(MATRIXXtrunc(germany,:),1);
YTgerm=Ygerm';

Yitaly=MATRIXXtrunc(italy,:);
YTitaly=Yitaly';

Yus=MATRIXXtrunc(us,:);
YTus=Yus';

Yafriques=sum(MATRIXXtrunc(afriques,:),1);
YTafriques=Yafriques';

Yuks=sum(MATRIXXtrunc(uks,:),1);

Ymaghrebs=sum(MATRIXXtrunc(maghrebs,:),1);

Yrussia=sum(MATRIXXtrunc(russia,:),1);
YTrussia=Yrussia';

YTindia=MATRIXXtrunc(italy,:)';
//espagne20   pays-bas   442
spain=[203];
netherland=[171];
netherlands=[168 169 170 171 ];
Yspain=MATRIXXtrunc(spain,:);
Ynetherl=MATRIXXtrunc(netherland,:);
YTspain=Yspain';
YTnetherl=Ynetherl';


YTsouthKorea=MATRIXXtrunc(southKorea,:)';
//pt p88
Noir=33;
//xset("background",Noir);
//plot( [X,X,X,X,X],[Ychines,Yfrances, Yitaly,Yus, Ygerm])
//big green p69
plot2d('onn', XT,[YTchines YTfrances YTitaly YTus YTgerm,YTspain,YTnetherl,YTafriques,YTrussia,YTindia,YTsouthKorea],[1 -2 -3 -4 -5 6 -7 2 3 4 5],"121","chines@frances@italy@us@germ@Spain@Netherlands@Afrique@Russia@India@south Korea")
xtitle('Covid19 evolution from 2020/1/22')
