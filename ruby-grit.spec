%define	pkgname	grit
Summary:	Ruby Git bindings
Name:		ruby-%{pkgname}
Version:	2.5.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	bb66887fe3eb7bfaef50c6b86bbabfc1
Patch0:		%{name}-nogems.patch
URL:		http://github.com/mojombo/grit
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grit gives you object oriented read/write access to Git repositories
via Ruby. The main goals are stability and performance. To this end,
some of the interactions with Git repositories are done by shelling
out to the system's `git` command, and other interactions are done
with pure Ruby reimplementations of core Git functionality. This
choice, however, is transparent to end users, and you need not know
which method is being used.

%prep
%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md API.txt History.txt PURE_TODO LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
%{_examplesdir}/%{name}-%{version}
