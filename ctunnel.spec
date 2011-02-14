Summary:	Crypto Tunnel for Proxying and Forwarding TCP/UDP Connections
Name:		ctunnel
Version:	0.6
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.nardcore.org/ctunnel/%{name}-%{version}.tar.gz
# Source0-md5:	23ba8758fb92dd71915b869ea82aa475
URL:		http://nardcore.org/ctunnel/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctunnel is a software for proxying and forwarding TCP connections via
a cryptographic tunnel.

ctunnel can be used to secure any existing TCP based protocol, such as
HTTP, VNC, Telnet, FTP, RSH, MySQL, etc, as well as UDP. You can even
tunnel SSH! (if you are really paranoid!).

You can also chain/bounce connections to any number of intermediary
hosts.ctunnel is a software for proxying and forwarding TCP
connections via a cryptographic tunnel.

%prep
%setup -q
sed -i 's/=.*-O2/=%{rpmcflags}/' src/Makefile

%build
%{__make} \
     CC="%{__cc}" 

%install
rm -rf $RPM_BUILD_ROOT

install -D src/ctunnel	$RPM_BUILD_ROOT%{_bindir}/ctunnel
install -D ctunnel.1	$RPM_BUILD_ROOT%{_mandir}/man1/ctunnel.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ctunnel
%{_mandir}/man1/*
