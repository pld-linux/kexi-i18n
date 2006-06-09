Summary:	Kexi - international support
Summary(pl):	Kexi - wsparcie dla wielu jêzyków
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
Kexi - wsparcie dla wielu jêzyków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Requires:	kde-i18n-base
Obsoletes:	kexi-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	Kexi - Afrikaans language support
Summary(pl):	Kexi - wsparcie dla jêzyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Afrikaans
Kexi  - Afrikaans language support.

%description Afrikaans -l pl
Kexi - wsparcie dla jêzyka afrykanerskiego.

%package Arabic
Summary:	Kexi - Arabic language support
Summary(pl):	Kexi - wsparcie dla jêzyka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
Kexi - Arabic language support.

%description Arabic -l pl
Kexi - wsparcie dla jêzyka arabskiego.

%package Azerbaijani
Summary:	Kexi - Azerbaijani language support
Summary(pl):	Kexi - wsparcie dla jêzyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
Kexi - Azerbaijani language support.

%description Azerbaijani -l pl
Kexi - wsparcie dla jêzyka azerskiego.

%package Bulgarian
Summary:	Kexi - Bulgarian language support
Summary(pl):	Kexi - wsparcie dla jêzyka bu³garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
Kexi - Bulgarian language support.

%description Bulgarian -l pl
Kexi - wsparcie dla jêzyka bu³garskiego.

%package Breton
Summary:	Kexi - Breton language support
Summary(pl):	Kexi - wsparcie dla jêzyka bretoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
Kexi - Breton language support.

%description Breton -l pl
Kexi - wsparcie dla jêzyka bretoñskiego.

%package Bosnian
Summary:	Kexi - Bosnian language support
Summary(pl):	Kexi - wsparcie dla jêzyka bo¶niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
Kexi - Bosnian language support.

%description Bosnian -l pl
Kexi - wsparcie dla jêzyka bo¶niackiego.

%package Catalan
Summary:	Kexi - Catalan language support
Summary(pl):	Kexi - wsparcie dla jêzyka kataloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
Kexi - Catalan language support.

%description Catalan -l pl
Kexi - wsparcie dla jêzyka kataloñskiego.

%package Czech
Summary:	Kexi - Czech language support
Summary(pl):	Kexi - wsparcie dla jêzyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
Kexi - Czech language support.

%description Czech -l pl
Kexi - wsparcie dla jêzyka czeskiego.

%package Cymraeg
Summary:	Kexi - Cymraeg language support
Summary(pl):	Kexi - wsparcie dla jêzyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
Kexi - Cymraeg language support.

%description Cymraeg -l pl
Kexi - wsparcie dla jêzyka walijskiego.

%package Danish
Summary:	Kexi - Danish language support
Summary(pl):	Kexi - wsparcie dla jêzyka duñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
Kexi - Danish language support.

%description Danish -l pl
Kexi - wsparcie dla jêzyka duñskiego.

%package German
Summary:	Kexi - German language support
Summary(pl):	Kexi - wsparcie dla jêzyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
Kexi - German language support.

%description German -l pl
Kexi - wsparcie dla jêzyka niemieckiego.

%package Greek
Summary:	Kexi - Greek language support
Summary(pl):	Kexi - wsparcie dla jêzyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
Kexi - Greek language support.

%description Greek -l pl
Kexi - wsparcie dla jêzyka greckiego.

%package English
Summary:	Kexi - English language support
Summary(pl):	Kexi - wsparcie dla jêzyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
Kexi - English language support.

%description English -l pl
Kexi - wsparcie dla jêzyka angielskiego.

%package English_UK
Summary:	Kexi - English (UK) language support
Summary(pl):	Kexi - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
Kexi - English (UK) language support.

%description English_UK -l pl
Kexi - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	Kexi - Esperanto language support
Summary(pl):	Kexi - wsparcie dla jêzyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
Kexi - Esperanto language support.

%description Esperanto -l pl
Kexi - wsparcie dla jêzyka esperanto.

%package Spanish
Summary:	Kexi - Spanish language support
Summary(pl):	Kexi - wsparcie dla jêzyka hiszpañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
Kexi - Spanish language support.

%description Spanish -l pl
Kexi - wsparcie dla jêzyka hiszpañskiego.

%package Estonian
Summary:	Kexi - Estonian language support
Summary(pl):	Kexi - wsparcie dla jêzyka estoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
Kexi - Estonian language support.

%description Estonian -l pl
Kexi - wsparcie dla jêzyka estoñskiego.

%package Basque
Summary:	Kexi - Basque language support
Summary(pl):	Kexi - wsparcie dla jêzyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
Kexi - Basque language support.

%description Basque -l pl
Kexi - wsparcie dla jêzyka baskijskiego.

%package Farsi
Summary:	Kexi - Farsi language support
Summary(pl):	Kexi - wsparcie dla jêzyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
Kexi - Farsi language support.

%description Farsi -l pl
Kexi - wsparcie dla jêzyka perskiego (farsi).


%package Finnish
Summary:	Kexi - Finnish language support
Summary(pl):	Kexi - wsparcie dla jêzyka fiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
Kexi - Finnish language support.

%description Finnish -l pl
Kexi - wsparcie dla jêzyka fiñskiego.

%package Faroese
Summary:	Kexi - Faroese language support
Summary(pl):	Kexi - wsparcie dla jêzyka faroezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Faroese
Kexi - Faroese language support.

%description Faroese -l pl
Kexi - wsparcie dla jêzyka faroezyjskiego.

%package French
Summary:	Kexi - French language support
Summary(pl):	Kexi - wsparcie dla jêzyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
Kexi - French language support.

%description French -l pl
Kexi - wsparcie dla jêzyka francuskiego.

%package Irish
Summary:	Kexi - Irish language support
Summary(pl):	Kexi - wsparcie dla jêzyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
Kexi - Irish language support.

%description Irish -l pl
Kexi - wsparcie dla jêzyka irlandzkiego.

%package Galician
Summary:	Kexi - Galician language support
Summary(pl):	Kexi - wsparcie dla jêzyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
Kexi - Galician language support.

%description Galician -l pl
Kexi - wsparcie dla jêzyka galicyjskiego.

%package Hindi
Summary:	Kexi - Hindi language support
Summary(pl):	Kexi - wsparcie dla jêzyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
Kexi - Hindi language support.

%description Hindi -l pl
Kexi - wsparcie dla jêzyka hindi.

%package Hebrew
Summary:	Kexi - Hebrew language support
Summary(pl):	Kexi - wsparcie dla jêzyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
Kexi - Hebrew language support.

%description Hebrew -l pl
Kexi - wsparcie dla jêzyka hebrajskiego.

%package Croatian
Summary:	Kexi - Croatian language support
Summary(pl):	Kexi - wsparcie dla jêzyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
Kexi - Croatian language support.

%description Croatian -l pl
Kexi - wsparcie dla jêzyka chorwackiego.

%package Hungarian
Summary:	Kexi - Hungarian language support
Summary(pl):	Kexi - wsparcie dla jêzyka wêgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
Kexi - Hungarian language support.

%description Hungarian -l pl
Kexi - wsparcie dla jêzyka wêgierskiego.

%package Upper_Sorbian
Summary:	Kexi - Upper Sorbian language support
Summary(pl):	Kexi - wsparcie dla jêzyka górno³u¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
Kexi - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
Kexi - wsparcie dla jêzyka górno³u¿yckiego.

%package Indonesian
Summary:	Kexi - Indonesian language support
Summary(pl):	Kexi - wsparcie dla jêzyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
Kexi - Indonesian language support.

%description Indonesian -l pl
Kexi - wsparcie dla jêzyka indonezyjskiego.

%package Icelandic
Summary:	Kexi - Icelandic language support
Summary(pl):	Kexi - wsparcie dla jêzyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
Kexi - Icelandic language support.

%description Icelandic -l pl
Kexi - wsparcie dla jêzyka islandzkiego.

%package Italian
Summary:	Kexi - Italian language support
Summary(pl):	Kexi - wsparcie dla jêzyka w³oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
Kexi - Italian language support.

%description Italian -l pl
Kexi - wsparcie dla jêzyka w³oskiego.

%package Japanese
Summary:	Kexi - Japanese language support
Summary(pl):	Kexi - wsparcie dla jêzyka japoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
Kexi - Japanese language support.

%description Japanese -l pl
Kexi - wsparcie dla jêzyka japoñskiego.

%package Korean
Summary:	Kexi - Korean language support
Summary(pl):	Kexi - wsparcie dla jêzyka koreañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
Kexi - Korean language support.

%description Korean -l pl
Kexi - wsparcie dla jêzyka koreañskiego.

%package Lithuanian
Summary:	Kexi - Lithuanian language support
Summary(pl):	Kexi - wsparcie dla jêzyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
Kexi - Lithuanian language support.

%description Lithuanian -l pl
Kexi - Wsparcie dla jêzyka litewskiego.

%package Lao
Summary:	Kexi - Lao language support
Summary(pl):	Kexi - wsparcie dla jêzyka laotañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
Kexi - lao language support.

%description Lao -l pl
Kexi - wsparcie dla jêzyka laotañskiego.

%package Latvian
Summary:	Kexi - Latvian language support
Summary(pl):	Kexi - wsparcie dla jêzyka ³otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
Kexi - Latvian language support.

%description Latvian -l pl
Kexi - wsparcie dla jêzyka ³otewskiego.

%package Maori
Summary:	Kexi - Maori language support
Summary(pl):	Kexi - wsparcie dla jêzyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
Kexi - Maori language support.

%description Maori -l pl
Kexi - wsparcie dla jêzyka maoryjskiego.

%package Macedonian
Summary:	Kexi - Macedonian language support
Summary(pl):	Kexi - wsparcie dla jêzyka macedoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
Kexi - Macedonian language support.

%description Macedonian -l pl
Kexi - wsparcie dla jêzyka macedoñskiego.

%package Malay
Summary:	Kexi - Malay language support
Summary(pl):	Kexi - wsparcie dla jêzyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
Kexi - Malay language support.

%description Malay -l pl
Kexi - wsparcie dla jêzyka malajskiego.

%package Maltese
Summary:	Kexi - Maltese language support
Summary(pl):	Kexi - wsparcie dla jêzyka maltañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
Kexi - Maltese language support.

%description Maltese -l pl
Kexi - wsparcie dla jêzyka maltañskiego.

%package Mongolian
Summary:	Kexi - Mongolian language support
Summary(pl):	Kexi - wsparcie dla jêzyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
Kexi - Mongolian language support.

%description Mongolian -l pl
Kexi - wsparcie dla jêzyka mongolskiego.

%package Dutch
Summary:	Kexi - Dutch language support
Summary(pl):	Kexi - wsparcie dla jêzyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
Kexi - Dutch language support.

%description Dutch -l pl
Kexi - wsparcie dla jêzyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	Kexi - Norwegian (Bokmaal) language support
Summary(pl):	Kexi - wsparcie dla jêzyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Bokmaal
Kexi - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
Kexi - wsparcie dla jêzyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	Kexi - Norwegian (Nynorsk) language support
Summary(pl):	Kexi - wsparcie dla jêzyka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
Kexi - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
Kexi - wsparcie dla jêzyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	Kexi - Northern Sotho language support
Summary(pl):	Kexi - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
Kexi - Northern Sotho language support.

%description Northern_Sotho -l pl
Kexi - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto.

%package Gascon_occitan
Summary:	Kexi - Occitan (Gascon) language support
Summary(pl):	Kexi - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
Kexi - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
Kexi - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego).

%package Polish
Summary:	Kexi - Polish language support
Summary(pl):	Kexi - wsparcie dla jêzyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
Kexi - Polish language support.

%description Polish -l pl
Kexi - wsparcie dla jêzyka polskiego.

%package Portuguese
Summary:	Kexi - Portuguese language support
Summary(pl):	Kexi - wsparcie dla jêzyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Portuguese
Kexi - Portuguese language support.

%description Portuguese -l pl
Kexi - wsparcie dla jêzyka portugalskiego.

%package Brazil_Portuguese
Summary:	Kexi - Portuguese (Brazil) language support
Summary(pl):	Kexi - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Brazil_Portuguese
Kexi - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
Kexi - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	Kexi - Romanian language support
Summary(pl):	Kexi - wsparcie dla jêzyka rumuñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
Kexi - Romanian language support.

%description Romanian -l pl
Kexi - wsparcie dla jêzyka rumuñskiego.

%package Russian
Summary:	Kexi - Russian language support
Summary(pl):	Kexi - wsparcie dla jêzyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
Kexi - Russian language support.

%description Russian -l pl
Kexi - wsparcie dla jêzyka rosyjskiego.

%package Swati
Summary:	Kexi - Swati language support
Summary(pl):	Kexi - wsparcie dla jêzyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
Kexi - Swati language support.

%description Swati -l pl
Kexi - wsparcie dla jêzyka swati.

%package Northern_Sami
Summary:	Kexi - Northern Sami language support
Summary(pl):	Kexi - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
Kexi - Northern Sami language support.

%description Northern_Sami -l pl
Kexi - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego).

%package Slovak
Summary:	Kexi - Slovak language support
Summary(pl):	Kexi - wsparcie dla jêzyka s³owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
Kexi - Slovak language support.

%description Slovak -l pl
Kexi - wsparcie dla jêzyka s³owackiego.

%package Slovenian
Summary:	Kexi - Slovenian language support
Summary(pl):	Kexi - wsparcie dla jêzyka s³oweñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
Kexi - Slovenian language support.

%description Slovenian -l pl
Kexi - wsparcie dla jêzyka s³oweñskiego.

%package Serbian
Summary:	Kexi - Serbian language support
Summary(pl):	Kexi - wsparcie dla jêzyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
Kexi - Serbian language support.

%description Serbian -l pl
Kexi - wsparcie dla jêzyka serbskiego.

%package Swedish
Summary:	Kexi - Swedish language support
Summary(pl):	Kexi - wsparcie dla jêzyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
Kexi - Swedish language support.

%description Swedish -l pl
Kexi - wsparcie dla jêzyka szwedzkiego.

%package Tamil
Summary:	Kexi - Tamil language support
Summary(pl):	Kexi - wsparcie dla jêzyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
Kexi - Tamil language support.

%description Tamil -l pl
Kexi - wsparcie dla jêzyka tamilskiego.

%package Tajik
Summary:	Kexi - Tajik language support
Summary(pl):	Kexi - wsparcie dla jêzyka tad¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
Kexi - Tajik language support.

%description Tajik -l pl
Kexi - wsparcie dla jêzyka tad¿yckiego.

%package Thai
Summary:	Kexi - Thai language support
Summary(pl):	Kexi - wsparcie dla jêzyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
Kexi - Thai language support.

%description Thai -l pl
Kexi - wsparcie dla jêzyka tajlandzkiego.

%package Turkish
Summary:	Kexi - Turkish language support
Summary(pl):	Kexi - wsparcie dla jêzyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
Kexi - Turkish language support.

%description Turkish -l pl
Kexi - wsparcie dla jêzyka tureckiego.

%package Ukrainian
Summary:	Kexi - Ukrainian language support
Summary(pl):	Kexi - wsparcie dla jêzyka ukraiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
Kexi - Ukrainian language support.

%description Ukrainian -l pl
Kexi - wsparcie dla jêzyka ukraiñskiego.

%package Uzbek
Summary:	Kexi - Uzbek language support
Summary(pl):	Kexi - wsparcie dla jêzyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
Kexi - Uzbek language support.

%description Uzbek -l pl
Kexi - wsparcie dla jêzyka uzbeckiego.

%package Venda
Summary:	Kexi - Venda language support
Summary(pl):	Kexi - wsparcie dla jêzyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
Kexi - Venda language support.

%description Venda -l pl
Kexi - wsparcie dla jêzyka venda.

%package Vietnamese
Summary:	Kexi - Vietnamese language support
Summary(pl):	Kexi - wsparcie dla jêzyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
Kexi - Vietnamese language support.

%description Vietnamese -l pl
Kexi - wsparcie dla jêzyka wietnamskiego.

%package Walloon
Summary:	Kexi - Walloon language support
Summary(pl):	Kexi - wsparcie dla jêzyka waloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
Kexi - Walloon language support.

%description Walloon -l pl
Kexi - wsparcie dla jêzyka waloñskiego.

%package Xhosa
Summary:	Kexi - Xhosa language support
Summary(pl):	Kexi - wsparcie dla jêzyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
Kexi - Xhosa language support.

%description Xhosa -l pl
Kexi - wsparcie dla jêzyka khosa.

%package Simplified_Chinese
Summary:	Kexi - simplified Chinese language support
Summary(pl):	Kexi - wsparcie dla uproszczonego jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
Kexi - simplified Chinese language support.

%description Simplified_Chinese -l pl
Kexi - wsparcie dla uproszczonego jêzyka chiñskiego.

%package Chinese
Summary:	Kexi - Chinese language support
Summary(pl):	Kexi - wsparcie dla jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
Kexi - Chinese language support.

%description Chinese -l pl
Kexi - wsparcie dla jêzyka chiñskiego.

%package Zulu
Summary:	Kexi - Zulu language support
Summary(pl):	Kexi - wsparcie dla jêzyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
Kexi - Zulu language support.

%description Zulu -l pl
Kexi - wsparcie dla jêzyka zuluskiego.

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
