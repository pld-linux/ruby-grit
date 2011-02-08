
%define gitrev 7609e74
%define gitauthor mojombo
%define gitname grit

Summary:	Ruby interface to Git
Name:		ruby-grit
Version:	2.2.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-v%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	5e6a2d136de6c66059d439f3e2a41b55
Patch0:		%{name}-nogems.patch
URL:		http://grit.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
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
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/grit.rb
%{ruby_rubylibdir}/grit
