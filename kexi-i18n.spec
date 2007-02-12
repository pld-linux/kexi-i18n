Summary:	Kexi - international support
Summary(pl.UTF-8):   Kexi - wsparcie dla wielu języków
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

%description -l pl.UTF-8
Kexi - wsparcie dla wielu języków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl.UTF-8):   Pusty metapakiet z obsoletes
Group:		X11/Applications
Requires:	kde-i18n-base
Obsoletes:	kexi-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl.UTF-8
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	Kexi - Afrikaans language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Afrikaans
Kexi  - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
Kexi - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	Kexi - Arabic language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
Kexi - Arabic language support.

%description Arabic -l pl.UTF-8
Kexi - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	Kexi - Azerbaijani language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
Kexi - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
Kexi - wsparcie dla języka azerskiego.

%package Bulgarian
Summary:	Kexi - Bulgarian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka bułgarskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
Kexi - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
Kexi - wsparcie dla języka bułgarskiego.

%package Breton
Summary:	Kexi - Breton language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka bretońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
Kexi - Breton language support.

%description Breton -l pl.UTF-8
Kexi - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	Kexi - Bosnian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka bośniackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
Kexi - Bosnian language support.

%description Bosnian -l pl.UTF-8
Kexi - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	Kexi - Catalan language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka katalońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
Kexi - Catalan language support.

%description Catalan -l pl.UTF-8
Kexi - wsparcie dla języka katalońskiego.

%package Czech
Summary:	Kexi - Czech language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
Kexi - Czech language support.

%description Czech -l pl.UTF-8
Kexi - wsparcie dla języka czeskiego.

%package Cymraeg
Summary:	Kexi - Cymraeg language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
Kexi - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
Kexi - wsparcie dla języka walijskiego.

%package Danish
Summary:	Kexi - Danish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka duńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
Kexi - Danish language support.

%description Danish -l pl.UTF-8
Kexi - wsparcie dla języka duńskiego.

%package German
Summary:	Kexi - German language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
Kexi - German language support.

%description German -l pl.UTF-8
Kexi - wsparcie dla języka niemieckiego.

%package Greek
Summary:	Kexi - Greek language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
Kexi - Greek language support.

%description Greek -l pl.UTF-8
Kexi - wsparcie dla języka greckiego.

%package English
Summary:	Kexi - English language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
Kexi - English language support.

%description English -l pl.UTF-8
Kexi - wsparcie dla języka angielskiego.

%package English_UK
Summary:	Kexi - English (UK) language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
Kexi - English (UK) language support.

%description English_UK -l pl.UTF-8
Kexi - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	Kexi - Esperanto language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
Kexi - Esperanto language support.

%description Esperanto -l pl.UTF-8
Kexi - wsparcie dla języka esperanto.

%package Spanish
Summary:	Kexi - Spanish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka hiszpańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
Kexi - Spanish language support.

%description Spanish -l pl.UTF-8
Kexi - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	Kexi - Estonian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka estońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
Kexi - Estonian language support.

%description Estonian -l pl.UTF-8
Kexi - wsparcie dla języka estońskiego.

%package Basque
Summary:	Kexi - Basque language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
Kexi - Basque language support.

%description Basque -l pl.UTF-8
Kexi - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	Kexi - Farsi language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
Kexi - Farsi language support.

%description Farsi -l pl.UTF-8
Kexi - wsparcie dla języka perskiego (farsi).


%package Finnish
Summary:	Kexi - Finnish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka fińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
Kexi - Finnish language support.

%description Finnish -l pl.UTF-8
Kexi - wsparcie dla języka fińskiego.

%package Faroese
Summary:	Kexi - Faroese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka faroezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Faroese
Kexi - Faroese language support.

%description Faroese -l pl.UTF-8
Kexi - wsparcie dla języka faroezyjskiego.

%package French
Summary:	Kexi - French language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
Kexi - French language support.

%description French -l pl.UTF-8
Kexi - wsparcie dla języka francuskiego.

%package Irish
Summary:	Kexi - Irish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
Kexi - Irish language support.

%description Irish -l pl.UTF-8
Kexi - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	Kexi - Galician language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
Kexi - Galician language support.

%description Galician -l pl.UTF-8
Kexi - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	Kexi - Hindi language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
Kexi - Hindi language support.

%description Hindi -l pl.UTF-8
Kexi - wsparcie dla języka hindi.

%package Hebrew
Summary:	Kexi - Hebrew language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
Kexi - Hebrew language support.

%description Hebrew -l pl.UTF-8
Kexi - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	Kexi - Croatian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
Kexi - Croatian language support.

%description Croatian -l pl.UTF-8
Kexi - wsparcie dla języka chorwackiego.

%package Hungarian
Summary:	Kexi - Hungarian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka węgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
Kexi - Hungarian language support.

%description Hungarian -l pl.UTF-8
Kexi - wsparcie dla języka węgierskiego.

%package Upper_Sorbian
Summary:	Kexi - Upper Sorbian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka górnołużyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
Kexi - Upper Sorbian language support.

%description Upper_Sorbian  -l pl.UTF-8
Kexi - wsparcie dla języka górnołużyckiego.

%package Indonesian
Summary:	Kexi - Indonesian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
Kexi - Indonesian language support.

%description Indonesian -l pl.UTF-8
Kexi - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	Kexi - Icelandic language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
Kexi - Icelandic language support.

%description Icelandic -l pl.UTF-8
Kexi - wsparcie dla języka islandzkiego.

%package Italian
Summary:	Kexi - Italian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka włoskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
Kexi - Italian language support.

%description Italian -l pl.UTF-8
Kexi - wsparcie dla języka włoskiego.

%package Japanese
Summary:	Kexi - Japanese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka japońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
Kexi - Japanese language support.

%description Japanese -l pl.UTF-8
Kexi - wsparcie dla języka japońskiego.

%package Korean
Summary:	Kexi - Korean language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka koreańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
Kexi - Korean language support.

%description Korean -l pl.UTF-8
Kexi - wsparcie dla języka koreańskiego.

%package Lithuanian
Summary:	Kexi - Lithuanian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
Kexi - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
Kexi - Wsparcie dla języka litewskiego.

%package Lao
Summary:	Kexi - Lao language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka laotańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
Kexi - lao language support.

%description Lao -l pl.UTF-8
Kexi - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	Kexi - Latvian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka łotewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
Kexi - Latvian language support.

%description Latvian -l pl.UTF-8
Kexi - wsparcie dla języka łotewskiego.

%package Maori
Summary:	Kexi - Maori language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
Kexi - Maori language support.

%description Maori -l pl.UTF-8
Kexi - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	Kexi - Macedonian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka macedońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
Kexi - Macedonian language support.

%description Macedonian -l pl.UTF-8
Kexi - wsparcie dla języka macedońskiego.

%package Malay
Summary:	Kexi - Malay language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
Kexi - Malay language support.

%description Malay -l pl.UTF-8
Kexi - wsparcie dla języka malajskiego.

%package Maltese
Summary:	Kexi - Maltese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka maltańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
Kexi - Maltese language support.

%description Maltese -l pl.UTF-8
Kexi - wsparcie dla języka maltańskiego.

%package Mongolian
Summary:	Kexi - Mongolian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
Kexi - Mongolian language support.

%description Mongolian -l pl.UTF-8
Kexi - wsparcie dla języka mongolskiego.

%package Dutch
Summary:	Kexi - Dutch language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
Kexi - Dutch language support.

%description Dutch -l pl.UTF-8
Kexi - wsparcie dla języka holenderskiego.

%package Norwegian_Bokmaal
Summary:	Kexi - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Bokmaal
Kexi - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
Kexi - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	Kexi - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
Kexi - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
Kexi - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	Kexi - Northern Sotho language support
Summary(pl.UTF-8):   Kexi - wsparcie dla północnej odmiany języka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
Kexi - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
Kexi - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_occitan
Summary:	Kexi - Occitan (Gascon) language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
Kexi - Occitan (Gascon) language support.

%description Gascon_occitan -l pl.UTF-8
Kexi - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Polish
Summary:	Kexi - Polish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
Kexi - Polish language support.

%description Polish -l pl.UTF-8
Kexi - wsparcie dla języka polskiego.

%package Portuguese
Summary:	Kexi - Portuguese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Portuguese
Kexi - Portuguese language support.

%description Portuguese -l pl.UTF-8
Kexi - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	Kexi - Portuguese (Brazil) language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Brazil_Portuguese
Kexi - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
Kexi - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	Kexi - Romanian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka rumuńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
Kexi - Romanian language support.

%description Romanian -l pl.UTF-8
Kexi - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	Kexi - Russian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
Kexi - Russian language support.

%description Russian -l pl.UTF-8
Kexi - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	Kexi - Swati language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
Kexi - Swati language support.

%description Swati -l pl.UTF-8
Kexi - wsparcie dla języka swati.

%package Northern_Sami
Summary:	Kexi - Northern Sami language support
Summary(pl.UTF-8):   Kexi - wsparcie dla północnego języka saami (lapońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
Kexi - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
Kexi - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	Kexi - Slovak language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka słowackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
Kexi - Slovak language support.

%description Slovak -l pl.UTF-8
Kexi - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	Kexi - Slovenian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka słoweńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
Kexi - Slovenian language support.

%description Slovenian -l pl.UTF-8
Kexi - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	Kexi - Serbian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
Kexi - Serbian language support.

%description Serbian -l pl.UTF-8
Kexi - wsparcie dla języka serbskiego.

%package Swedish
Summary:	Kexi - Swedish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
Kexi - Swedish language support.

%description Swedish -l pl.UTF-8
Kexi - wsparcie dla języka szwedzkiego.

%package Tamil
Summary:	Kexi - Tamil language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
Kexi - Tamil language support.

%description Tamil -l pl.UTF-8
Kexi - wsparcie dla języka tamilskiego.

%package Tajik
Summary:	Kexi - Tajik language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka tadżyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
Kexi - Tajik language support.

%description Tajik -l pl.UTF-8
Kexi - wsparcie dla języka tadżyckiego.

%package Thai
Summary:	Kexi - Thai language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
Kexi - Thai language support.

%description Thai -l pl.UTF-8
Kexi - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	Kexi - Turkish language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
Kexi - Turkish language support.

%description Turkish -l pl.UTF-8
Kexi - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	Kexi - Ukrainian language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka ukraińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
Kexi - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
Kexi - wsparcie dla języka ukraińskiego.

%package Uzbek
Summary:	Kexi - Uzbek language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
Kexi - Uzbek language support.

%description Uzbek -l pl.UTF-8
Kexi - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	Kexi - Venda language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
Kexi - Venda language support.

%description Venda -l pl.UTF-8
Kexi - wsparcie dla języka venda.

%package Vietnamese
Summary:	Kexi - Vietnamese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
Kexi - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
Kexi - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	Kexi - Walloon language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka walońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
Kexi - Walloon language support.

%description Walloon -l pl.UTF-8
Kexi - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	Kexi - Xhosa language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
Kexi - Xhosa language support.

%description Xhosa -l pl.UTF-8
Kexi - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	Kexi - simplified Chinese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla uproszczonego języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
Kexi - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
Kexi - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	Kexi - Chinese language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
Kexi - Chinese language support.

%description Chinese -l pl.UTF-8
Kexi - wsparcie dla języka chińskiego.

%package Zulu
Summary:	Kexi - Zulu language support
Summary(pl.UTF-8):   Kexi - wsparcie dla języka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
Kexi - Zulu language support.

%description Zulu -l pl.UTF-8
Kexi - wsparcie dla języka zuluskiego.

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
