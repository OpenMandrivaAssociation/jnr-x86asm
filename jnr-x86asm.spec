Name:		jnr-x86asm
Version:	1.0.2
Release:	6
Summary:	Pure Java x86 and x86_64 assembler
Group:		Development/Java
License:	MIT
URL:		https://github.com/jnr/jnr-x86asm
Source0:	https://github.com/jnr/jnr-x86asm/archive/refs/tags/%{version}.tar.gz

BuildArch:	noarch
BuildSystem:	maven

%description
Pure Java assembler for x86 and x86_64, used by jnr-ffi.

%prep
%setup -q -n jnr-x86asm-%{version}

%files -f .mfiles
%doc LICENSE README
