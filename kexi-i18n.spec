Summary:	Kexi - international support
Summary(pl):	Kexi - wsparcie dla wielu j�zyk�w
Name:		kexi-i18n
Version:	0.1
%define	_snap	20050408
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	f53cabc0c71ece001851adecab27e328
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2
BuildArch:	noarch
Obsoletes:	kexi-i18n-base
Obsoletes:	kexi-i18n-Brazil_Portuguese
Obsoletes:	kexi-i18n-Breton
Obsoletes:	kexi-i18n-Bulgarian
Obsoletes:	kexi-i18n-Catalan
Obsoletes:	kexi-i18n-Croatian
Obsoletes:	kexi-i18n-Cymraeg
Obsoletes:	kexi-i18n-Czech
Obsoletes:	kexi-i18n-Danish
Obsoletes:	kexi-i18n-Dutch
Obsoletes:	kexi-i18n-English_UK
Obsoletes:	kexi-i18n-Estonian
Obsoletes:	kexi-i18n-Faroese
Obsoletes:	kexi-i18n-French
Obsoletes:	kexi-i18n-German
Obsoletes:	kexi-i18n-Greek
Obsoletes:	kexi-i18n-Hebrew
Obsoletes:	kexi-i18n-Hungarian
Obsoletes:	kexi-i18n-Irish
Obsoletes:	kexi-i18n-Italian
Obsoletes:	kexi-i18n-Lao
Obsoletes:	kexi-i18n-Norwegian_Bokmaal
Obsoletes:	kexi-i18n-Norwegian_Nynorsk
Obsoletes:	kexi-i18n-Polish
Obsoletes:	kexi-i18n-Portuguese
Obsoletes:	kexi-i18n-Romanian
Obsoletes:	kexi-i18n-Russian
Obsoletes:	kexi-i18n-Serbian
Obsoletes:	kexi-i18n-Simplified_Chinese
Obsoletes:	kexi-i18n-Slovak
Obsoletes:	kexi-i18n-Slovenian
Obsoletes:	kexi-i18n-Spanish
Obsoletes:	kexi-i18n-Swedish
Obsoletes:	kexi-i18n-Tajik
Obsoletes:	kexi-i18n-Tamil
Obsoletes:	kexi-i18n-Turkish
Obsoletes:	kexi-i18n-Uzbek
Obsoletes:	kexi-i18n-Zulu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kexi - international language support.

%description -l pl
Kexi - wsparcie dla wielu j�zyk�w.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Requires:	kde-i18n-base
Obsoletes:	kexi-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakiet�w i18n.

%package Afrikaans
Summary:	Kexi - Afrikaans language support
Summary(pl):	Kexi - wsparcie dla j�zyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Afrikaans
Kexi  - Afrikaans language support.

%description Afrikaans -l pl
Kexi - wsparcie dla j�zyka afrykanerskiego.

%package Arabic
Summary:	Kexi - Arabic language support
Summary(pl):	Kexi - wsparcie dla j�zyka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
Kexi - Arabic language support.

%description Arabic -l pl
Kexi - wsparcie dla j�zyka arabskiego.

%package Azerbaijani
Summary:	Kexi - Azerbaijani language support
Summary(pl):	Kexi - wsparcie dla j�zyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
Kexi - Azerbaijani language support.

%description Azerbaijani -l pl
Kexi - wsparcie dla j�zyka azerskiego.

%package Bulgarian
Summary:	Kexi - Bulgarian language support
Summary(pl):	Kexi - wsparcie dla j�zyka bu�garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
Kexi - Bulgarian language support.

%description Bulgarian -l pl
Kexi - wsparcie dla j�zyka bu�garskiego.

%package Breton
Summary:	Kexi - Breton language support
Summary(pl):	Kexi - wsparcie dla j�zyka breto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
Kexi - Breton language support.

%description Breton -l pl
Kexi - wsparcie dla j�zyka breto�skiego.

%package Bosnian
Summary:	Kexi - Bosnian language support
Summary(pl):	Kexi - wsparcie dla j�zyka bo�niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
Kexi - Bosnian language support.

%description Bosnian -l pl
Kexi - wsparcie dla j�zyka bo�niackiego.

%package Catalan
Summary:	Kexi - Catalan language support
Summary(pl):	Kexi - wsparcie dla j�zyka katalo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
Kexi - Catalan language support.

%description Catalan -l pl
Kexi - wsparcie dla j�zyka katalo�skiego.

%package Czech
Summary:	Kexi - Czech language support
Summary(pl):	Kexi - wsparcie dla j�zyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
Kexi - Czech language support.

%description Czech -l pl
Kexi - wsparcie dla j�zyka czeskiego.

%package Cymraeg
Summary:	Kexi - Cymraeg language support
Summary(pl):	Kexi - wsparcie dla j�zyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
Kexi - Cymraeg language support.

%description Cymraeg -l pl
Kexi - wsparcie dla j�zyka walijskiego.

%package Danish
Summary:	Kexi - Danish language support
Summary(pl):	Kexi - wsparcie dla j�zyka du�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
Kexi - Danish language support.

%description Danish -l pl
Kexi - wsparcie dla j�zyka du�skiego.

%package German
Summary:	Kexi - German language support
Summary(pl):	Kexi - wsparcie dla j�zyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
Kexi - German language support.

%description German -l pl
Kexi - wsparcie dla j�zyka niemieckiego.

%package Greek
Summary:	Kexi - Greek language support
Summary(pl):	Kexi - wsparcie dla j�zyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
Kexi - Greek language support.

%description Greek -l pl
Kexi - wsparcie dla j�zyka greckiego.

%package English
Summary:	Kexi - English language support
Summary(pl):	Kexi - wsparcie dla j�zyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
Kexi - English language support.

%description English -l pl
Kexi - wsparcie dla j�zyka angielskiego.

%package English_UK
Summary:	Kexi - English (UK) language support
Summary(pl):	Kexi - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
Kexi - English (UK) language support.

%description English_UK -l pl
Kexi - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	Kexi - Esperanto language support
Summary(pl):	Kexi - wsparcie dla j�zyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
Kexi - Esperanto language support.

%description Esperanto -l pl
Kexi - wsparcie dla j�zyka esperanto.

%package Spanish
Summary:	Kexi - Spanish language support
Summary(pl):	Kexi - wsparcie dla j�zyka hiszpa�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
Kexi - Spanish language support.

%description Spanish -l pl
Kexi - wsparcie dla j�zyka hiszpa�skiego.

%package Estonian
Summary:	Kexi - Estonian language support
Summary(pl):	Kexi - wsparcie dla j�zyka esto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
Kexi - Estonian language support.

%description Estonian -l pl
Kexi - wsparcie dla j�zyka esto�skiego.

%package Basque
Summary:	Kexi - Basque language support
Summary(pl):	Kexi - wsparcie dla j�zyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
Kexi - Basque language support.

%description Basque -l pl
Kexi - wsparcie dla j�zyka baskijskiego.

%package Farsi
Summary:	Kexi - Farsi language support
Summary(pl):	Kexi - wsparcie dla j�zyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
Kexi - Farsi language support.

%description Farsi -l pl
Kexi - wsparcie dla j�zyka perskiego (farsi).


%package Finnish
Summary:	Kexi - Finnish language support
Summary(pl):	Kexi - wsparcie dla j�zyka fi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
Kexi - Finnish language support.

%description Finnish -l pl
Kexi - wsparcie dla j�zyka fi�skiego.

%package Faroese
Summary:	Kexi - Faroese language support
Summary(pl):	Kexi - wsparcie dla j�zyka faroezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Faroese
Kexi - Faroese language support.

%description Faroese -l pl
Kexi - wsparcie dla j�zyka faroezyjskiego.

%package French
Summary:	Kexi - French language support
Summary(pl):	Kexi - wsparcie dla j�zyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
Kexi - French language support.

%description French -l pl
Kexi - wsparcie dla j�zyka francuskiego.

%package Irish
Summary:	Kexi - Irish language support
Summary(pl):	Kexi - wsparcie dla j�zyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
Kexi - Irish language support.

%description Irish -l pl
Kexi - wsparcie dla j�zyka irlandzkiego.

%package Galician
Summary:	Kexi - Galician language support
Summary(pl):	Kexi - wsparcie dla j�zyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
Kexi - Galician language support.

%description Galician -l pl
Kexi - wsparcie dla j�zyka galicyjskiego.

%package Hindi
Summary:	Kexi - Hindi language support
Summary(pl):	Kexi - wsparcie dla j�zyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
Kexi - Hindi language support.

%description Hindi -l pl
Kexi - wsparcie dla j�zyka hindi.

%package Hebrew
Summary:	Kexi - Hebrew language support
Summary(pl):	Kexi - wsparcie dla j�zyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
Kexi - Hebrew language support.

%description Hebrew -l pl
Kexi - wsparcie dla j�zyka hebrajskiego.

%package Croatian
Summary:	Kexi - Croatian language support
Summary(pl):	Kexi - wsparcie dla j�zyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
Kexi - Croatian language support.

%description Croatian -l pl
Kexi - wsparcie dla j�zyka chorwackiego.

%package Hungarian
Summary:	Kexi - Hungarian language support
Summary(pl):	Kexi - wsparcie dla j�zyka w�gierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
Kexi - Hungarian language support.

%description Hungarian -l pl
Kexi - wsparcie dla j�zyka w�gierskiego.

%package Upper_Sorbian
Summary:	Kexi - Upper Sorbian language support
Summary(pl):	Kexi - wsparcie dla j�zyka g�rno�u�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
Kexi - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
Kexi - wsparcie dla j�zyka g�rno�u�yckiego.

%package Indonesian
Summary:	Kexi - Indonesian language support
Summary(pl):	Kexi - wsparcie dla j�zyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
Kexi - Indonesian language support.

%description Indonesian -l pl
Kexi - wsparcie dla j�zyka indonezyjskiego.

%package Icelandic
Summary:	Kexi - Icelandic language support
Summary(pl):	Kexi - wsparcie dla j�zyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
Kexi - Icelandic language support.

%description Icelandic -l pl
Kexi - wsparcie dla j�zyka islandzkiego.

%package Italian
Summary:	Kexi - Italian language support
Summary(pl):	Kexi - wsparcie dla j�zyka w�oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
Kexi - Italian language support.

%description Italian -l pl
Kexi - wsparcie dla j�zyka w�oskiego.

%package Japanese
Summary:	Kexi - Japanese language support
Summary(pl):	Kexi - wsparcie dla j�zyka japo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
Kexi - Japanese language support.

%description Japanese -l pl
Kexi - wsparcie dla j�zyka japo�skiego.

%package Korean
Summary:	Kexi - Korean language support
Summary(pl):	Kexi - wsparcie dla j�zyka korea�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
Kexi - Korean language support.

%description Korean -l pl
Kexi - wsparcie dla j�zyka korea�skiego.

%package Lithuanian
Summary:	Kexi - Lithuanian language support
Summary(pl):	Kexi - wsparcie dla j�zyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
Kexi - Lithuanian language support.

%description Lithuanian -l pl
Kexi - Wsparcie dla j�zyka litewskiego.

%package Lao
Summary:	Kexi - Lao language support
Summary(pl):	Kexi - wsparcie dla j�zyka laota�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
Kexi - lao language support.

%description Lao -l pl
Kexi - wsparcie dla j�zyka laota�skiego.

%package Latvian
Summary:	Kexi - Latvian language support
Summary(pl):	Kexi - wsparcie dla j�zyka �otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
Kexi - Latvian language support.

%description Latvian -l pl
Kexi - wsparcie dla j�zyka �otewskiego.

%package Maori
Summary:	Kexi - Maori language support
Summary(pl):	Kexi - wsparcie dla j�zyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
Kexi - Maori language support.

%description Maori -l pl
Kexi - wsparcie dla j�zyka maoryjskiego.

%package Macedonian
Summary:	Kexi - Macedonian language support
Summary(pl):	Kexi - wsparcie dla j�zyka macedo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
Kexi - Macedonian language support.

%description Macedonian -l pl
Kexi - wsparcie dla j�zyka macedo�skiego.

%package Malay
Summary:	Kexi - Malay language support
Summary(pl):	Kexi - wsparcie dla j�zyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
Kexi - Malay language support.

%description Malay -l pl
Kexi - wsparcie dla j�zyka malajskiego.

%package Maltese
Summary:	Kexi - Maltese language support
Summary(pl):	Kexi - wsparcie dla j�zyka malta�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
Kexi - Maltese language support.

%description Maltese -l pl
Kexi - wsparcie dla j�zyka malta�skiego.

%package Mongolian
Summary:	Kexi - Mongolian language support
Summary(pl):	Kexi - wsparcie dla j�zyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
Kexi - Mongolian language support.

%description Mongolian -l pl
Kexi - wsparcie dla j�zyka mongolskiego.

%package Dutch
Summary:	Kexi - Dutch language support
Summary(pl):	Kexi - wsparcie dla j�zyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
Kexi - Dutch language support.

%description Dutch -l pl
Kexi - wsparcie dla j�zyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	Kexi - Norwegian (Bokmaal) language support
Summary(pl):	Kexi - wsparcie dla j�zyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Bokmaal
Kexi - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
Kexi - wsparcie dla j�zyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	Kexi - Norwegian (Nynorsk) language support
Summary(pl):	Kexi - wsparcie dla j�zyka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
Kexi - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
Kexi - wsparcie dla j�zyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	Kexi - Northern Sotho language support
Summary(pl):	Kexi - wsparcie dla p�nocnej odmiany j�zyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
Kexi - Northern Sotho language support.

%description Northern_Sotho -l pl
Kexi - wsparcie dla p�nocnej odmiany j�zyka ludu Soto.

%package Gascon_occitan
Summary:	Kexi - Occitan (Gascon) language support
Summary(pl):	Kexi - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
Kexi - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
Kexi - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego).

%package Polish
Summary:	Kexi - Polish language support
Summary(pl):	Kexi - wsparcie dla j�zyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
Kexi - Polish language support.

%description Polish -l pl
Kexi - wsparcie dla j�zyka polskiego.

%package Portuguese
Summary:	Kexi - Portuguese language support
Summary(pl):	Kexi - wsparcie dla j�zyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Portuguese
Kexi - Portuguese language support.

%description Portuguese -l pl
Kexi - wsparcie dla j�zyka portugalskiego.

%package Brazil_Portuguese
Summary:	Kexi - Portuguese (Brazil) language support
Summary(pl):	Kexi - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Brazil_Portuguese
Kexi - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
Kexi - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	Kexi - Romanian language support
Summary(pl):	Kexi - wsparcie dla j�zyka rumu�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
Kexi - Romanian language support.

%description Romanian -l pl
Kexi - wsparcie dla j�zyka rumu�skiego.

%package Russian
Summary:	Kexi - Russian language support
Summary(pl):	Kexi - wsparcie dla j�zyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
Kexi - Russian language support.

%description Russian -l pl
Kexi - wsparcie dla j�zyka rosyjskiego.

%package Swati
Summary:	Kexi - Swati language support
Summary(pl):	Kexi - wsparcie dla j�zyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
Kexi - Swati language support.

%description Swati -l pl
Kexi - wsparcie dla j�zyka swati.

%package Northern_Sami
Summary:	Kexi - Northern Sami language support
Summary(pl):	Kexi - wsparcie dla p�nocnego j�zyka saami (lapo�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
Kexi - Northern Sami language support.

%description Northern_Sami -l pl
Kexi - wsparcie dla p�nocnego j�zyka saami (lapo�skiego).

%package Slovak
Summary:	Kexi - Slovak language support
Summary(pl):	Kexi - wsparcie dla j�zyka s�owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
Kexi - Slovak language support.

%description Slovak -l pl
Kexi - wsparcie dla j�zyka s�owackiego.

%package Slovenian
Summary:	Kexi - Slovenian language support
Summary(pl):	Kexi - wsparcie dla j�zyka s�owe�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
Kexi - Slovenian language support.

%description Slovenian -l pl
Kexi - wsparcie dla j�zyka s�owe�skiego.

%package Serbian
Summary:	Kexi - Serbian language support
Summary(pl):	Kexi - wsparcie dla j�zyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
Kexi - Serbian language support.

%description Serbian -l pl
Kexi - wsparcie dla j�zyka serbskiego.

%package Swedish
Summary:	Kexi - Swedish language support
Summary(pl):	Kexi - wsparcie dla j�zyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
Kexi - Swedish language support.

%description Swedish -l pl
Kexi - wsparcie dla j�zyka szwedzkiego.

%package Tamil
Summary:	Kexi - Tamil language support
Summary(pl):	Kexi - wsparcie dla j�zyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
Kexi - Tamil language support.

%description Tamil -l pl
Kexi - wsparcie dla j�zyka tamilskiego.

%package Tajik
Summary:	Kexi - Tajik language support
Summary(pl):	Kexi - wsparcie dla j�zyka tad�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
Kexi - Tajik language support.

%description Tajik -l pl
Kexi - wsparcie dla j�zyka tad�yckiego.

%package Thai
Summary:	Kexi - Thai language support
Summary(pl):	Kexi - wsparcie dla j�zyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
Kexi - Thai language support.

%description Thai -l pl
Kexi - wsparcie dla j�zyka tajlandzkiego.

%package Turkish
Summary:	Kexi - Turkish language support
Summary(pl):	Kexi - wsparcie dla j�zyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
Kexi - Turkish language support.

%description Turkish -l pl
Kexi - wsparcie dla j�zyka tureckiego.

%package Ukrainian
Summary:	Kexi - Ukrainian language support
Summary(pl):	Kexi - wsparcie dla j�zyka ukrai�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
Kexi - Ukrainian language support.

%description Ukrainian -l pl
Kexi - wsparcie dla j�zyka ukrai�skiego.

%package Uzbek
Summary:	Kexi - Uzbek language support
Summary(pl):	Kexi - wsparcie dla j�zyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
Kexi - Uzbek language support.

%description Uzbek -l pl
Kexi - wsparcie dla j�zyka uzbeckiego.

%package Venda
Summary:	Kexi - Venda language support
Summary(pl):	Kexi - wsparcie dla j�zyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
Kexi - Venda language support.

%description Venda -l pl
Kexi - wsparcie dla j�zyka venda.

%package Vietnamese
Summary:	Kexi - Vietnamese language support
Summary(pl):	Kexi - wsparcie dla j�zyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
Kexi - Vietnamese language support.

%description Vietnamese -l pl
Kexi - wsparcie dla j�zyka wietnamskiego.

%package Walloon
Summary:	Kexi - Walloon language support
Summary(pl):	Kexi - wsparcie dla j�zyka walo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
Kexi - Walloon language support.

%description Walloon -l pl
Kexi - wsparcie dla j�zyka walo�skiego.

%package Xhosa
Summary:	Kexi - Xhosa language support
Summary(pl):	Kexi - wsparcie dla j�zyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
Kexi - Xhosa language support.

%description Xhosa -l pl
Kexi - wsparcie dla j�zyka khosa.

%package Simplified_Chinese
Summary:	Kexi - simplified Chinese language support
Summary(pl):	Kexi - wsparcie dla uproszczonego j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
Kexi - simplified Chinese language support.

%description Simplified_Chinese -l pl
Kexi - wsparcie dla uproszczonego j�zyka chi�skiego.

%package Chinese
Summary:	Kexi - Chinese language support
Summary(pl):	Kexi - wsparcie dla j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
Kexi - Chinese language support.

%description Chinese -l pl
Kexi - wsparcie dla j�zyka chi�skiego.

%package Zulu
Summary:	Kexi - Zulu language support
Summary(pl):	Kexi - wsparcie dla j�zyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
Kexi - Zulu language support.

%description Zulu -l pl
Kexi - wsparcie dla j�zyka zuluskiego.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

#Install locales
for dir in *; do
        [ ! -d "$dir" ] && continue
        install -d $RPM_BUILD_ROOT%{_datadir}/locale/$dir/LC_MESSAGES
        install $dir/kexi.mo $RPM_BUILD_ROOT%{_datadir}/locale/$dir/LC_MESSAGES/
done

FindLang() {
#    $1 - short language name
#    $2 - long language name

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/locale/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$1" ]; then
#       echo "%lang($1) %{_datadir}/locale/$1/[cef]*" >> "$2.lang"
       echo "%lang($1) %{_datadir}/locale/$1/LC_MESSAGES/*.mo" >> "$2.lang"
    fi
}

##FindLang af Afrikaans
##FindLang ar Arabic
##FindLang az Azerbaijani
FindLang bg Bulgarian
FindLang br Breton
##FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
##FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
##FindLang eu Basque
##FindLang fa Farsi
##FindLang fi Finnish
FindLang fo Faroese
FindLang fr French
FindLang ga Irish
##FindLang gl Galician
FindLang he Hebrew
##FindLang hsb Upper_Sorbian
##FindLang hi Hindi
FindLang hr Croatian
FindLang hu Hungarian
# FindLang id Indonesian
##FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
## FindLang ko Korean
##FindLang lt Lithuanian
FindLang lo Lao
## FindLang lv Latvian
# FindLang mi Maori
##FindLang mk Macedonian
##FindLang mn Mongolian
##FindLang ms Malay
##FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nl Dutch
FindLang nn Norwegian_Nynorsk
#indLang nso Northern_Sotho
# FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
FindLang ro Romanian
FindLang ru Russian
##FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sv Swedish
FindLang ta Tamil
FindLang tg Tajik
FindLang th Thai
FindLang tr Turkish
##FindLang uk Ukrainian
FindLang uz Uzbek
FindLang ven Venda
##FindLang vi Vietnamese
##FindLang wa Walloon
##FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
##FindLang zh_TW Chinese
FindLang zu Zulu

%find_lang kexi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kexi.lang
%defattr(644,root,root,755)
%files base
%defattr(644,root,root,755)
#%%files -f Afrikaans.lang Afrikaans
#%%defattr(644,root,root,755)
#%%files -f Arabic.lang Arabic
##%files -f Azerbaijani.lang Azerbaijani
%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)
%files -f Breton.lang Breton
%defattr(644,root,root,755)
##%files -f Bosnian.lang Bosnian
%files -f Catalan.lang Catalan
%defattr(644,root,root,755)
%files -f Czech.lang Czech
%defattr(644,root,root,755)
%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)
%files -f Danish.lang Danish
%defattr(644,root,root,755)
%files -f German.lang German
%defattr(644,root,root,755)
%files -f Greek.lang Greek
%defattr(644,root,root,755)
# %files -f English.lang English
%files -f English_UK.lang English_UK
%defattr(644,root,root,755)
#%%files -f Esperanto.lang Esperanto
#%%defattr(644,root,root,755)
%files -f Spanish.lang Spanish
%defattr(644,root,root,755)
%files -f Estonian.lang Estonian
%defattr(644,root,root,755)
##%files -f Basque.lang Basque
#%%files -f Farsi.lang Farsi
#%%defattr(644,root,root,755)
#%%files -f Finnish.lang Finnish
#%%defattr(644,root,root,755)
%files -f Faroese.lang Faroese
%defattr(644,root,root,755)
%files -f French.lang French
%defattr(644,root,root,755)
%files -f Irish.lang Irish
%defattr(644,root,root,755)
##%files -f Galician.lang Galician
##%files -f Hindi.lang Hindi
%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)
#%%files -f Upper_Sorbian.lang Upper_Sorbian
#%%defattr(644,root,root,755)
%files -f Croatian.lang Croatian
%defattr(644,root,root,755)
%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)
##%files -f Indonesian.lang Indonesian
#%%files -f Icelandic.lang Icelandic
%files -f Italian.lang Italian
%defattr(644,root,root,755)
#%%files -f Japanese.lang Japanese
#%%defattr(644,root,root,755)
##%files -f Korean.lang Korean
%files -f Lao.lang Lao
%defattr(644,root,root,755)
#%%files -f Lithuanian.lang Lithuanian
##%files -f Latvian.lang Latvian
#%%files -f Maltese.lang Maltese
#%%defattr(644,root,root,755)
##%files -f Malay.lang Malay
##%files -f Mongolian.lang Mongolian
# %files -f Maori.lang Maori
#%%files -f Macedonian.lang Macedonian
%files -f Dutch.lang Dutch
%defattr(644,root,root,755)
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)
#%%files -f Northern_Sotho.lang Northern_Sotho
# %files -f Gascon_occitan.lang Gascon_occitan
%files -f Polish.lang Polish
%defattr(644,root,root,755)
#%%{_datadir}/services/searchproviders/*.desktop
%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)
%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)
%files -f Romanian.lang Romanian
%defattr(644,root,root,755)
%files -f Russian.lang Russian
%defattr(644,root,root,755)
#%%files -f Northern_Sami.lang Northern_Sami
#%%defattr(644,root,root,755)
#%%files -f Swati.lang Swati
%files -f Slovak.lang Slovak
%defattr(644,root,root,755)
%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)
%files -f Serbian.lang Serbian
%defattr(644,root,root,755)
%files -f Swedish.lang Swedish
%defattr(644,root,root,755)
%files -f Tamil.lang Tamil
%defattr(644,root,root,755)
%files -f Tajik.lang Tajik
%defattr(644,root,root,755)
#%%files -f Thai.lang Thai
#%%defattr(644,root,root,755)
%files -f Turkish.lang Turkish
%defattr(644,root,root,755)
##%files -f Ukrainian.lang Ukrainian
%files -f Uzbek.lang Uzbek
%defattr(644,root,root,755)
#%%files -f Venda.lang Venda
#%%defattr(644,root,root,755)
#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon
#%%files -f Xhosa.lang Xhosa
#%%defattr(644,root,root,755)
%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)
#%%files -f Chinese.lang Chinese
#%%defattr(644,root,root,755)
%files -f Zulu.lang Zulu
%defattr(644,root,root,755)
