//from https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
//filename = fullfile( 'D:\Telecharg\time_series_2019-ncov-Confirmed.csv');
//filename = fullfile( 'time_series_2019-ncov-Confirmed.csv');
//DEPRECATED  src file
filename = fullfile( 'time_series_2019-ncov-Confirmed.csv');

MATRIXX = csvRead ( filename,",","double" );
//X=MATRIXX(1:1,:)
X=1:size(MATRIXX)(1,2);
XT=X.';
chines  = [   156.    160.    161.    162.    163.    164.    165.    166.    168.    169.    170.    171.    173.    174.    175.    176.    177.    178.    179.    180.    181.    182.    183.    184.    185.    186.    187.    189.    190.    191.    195.    196.   204.];

france=[159];
frances=[159 200 207 407 432 440 444 452 464];
germany=[13];
italy=[18];
us=[100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 416 419 433 450];
afriques=[67,79,87,414,427,428,448,449,483];
uks=[202 210 405 451 461 465 477 ];
maghrebs=[15,209];
russia=[194];

india=[17];
southKorea=[158];
//regression shape 1,9 vers 3*3 :  INC3=matrix(INC,3,3) ; INC4=INC3.' trans.'

//POUB=1:9
Ychines=sum(MATRIXX(chines,:),1);
YTchines=Ychines';

Yfrance=MATRIXX(france,:);

Yfrances=sum(MATRIXX(frances,:),1);
YTfrances=Yfrances';

Ygerm=sum(MATRIXX(germany,:),1);
YTgerm=Ygerm';

Yitaly=MATRIXX(italy,:);
YTitaly=Yitaly';

Yus=sum(MATRIXX(us,:),1);
YTus=Yus';

Yafriques=sum(MATRIXX(afriques,:),1);
YTafriques=Yafriques';

Yuks=sum(MATRIXX(uks,:),1);

Ymaghrebs=sum(MATRIXX(maghrebs,:),1);

Yrussia=sum(MATRIXX(russia,:),1);
YTrussia=Yrussia';

YTindia=MATRIXX(italy,:)';
//espagne20   pays-bas   442
spain=[20];
netherlands=[442];
Yspain=MATRIXX(spain,:);
Ynetherl=MATRIXX(netherlands,:);
YTspain=Yspain';
YTnetherl=Ynetherl';


YTsouthKorea=MATRIXX(southKorea,:)';
//pt p88
Noir=33;
//xset("background",Noir);
//plot( [X,X,X,X,X],[Ychines,Yfrances, Yitaly,Yus, Ygerm])
//big green p69
plot2d('onn', XT,[YTchines YTfrances YTitaly YTus YTgerm,YTspain,YTnetherl,YTafriques,YTrussia,YTindia,YTsouthKorea],[1 -2 -3 -4 -5 6 -7 2 3 4 5],"121","chines@frances@italy@us@germ@Spain@Netherlands@Afrique@Russia@India@south Korea")
xtitle('Covid19 Le20200325')
