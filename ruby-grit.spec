%define	pkgname	grit
Summary:	Ruby Git bindings
Name:		ruby-%{pkgname}
Version:	2.4.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c8bee515d6eace9aec7336e0ac6b0768
Patch0:		%{name}-nogems.patch
URL:		http://github.com/mojombo/grit
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-diff-lcs < 2
Requires:	ruby-diff-lcs >= 1.1
Requires:	ruby-mime-types < 2
Requires:	ruby-mime-types >= 1.15
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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md API.txt History.txt PURE_TODO LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{_examplesdir}/%{name}-%{version}
