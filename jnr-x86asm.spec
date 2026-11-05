Name:		jnr-x86asm
Version:	1.0.2
Release:	6
Summary:	Pure Java x86 and x86_64 assembler
Group:		Development/Java
License:	MIT
URL:		https://github.com/jnr/jnr-x86asm
Source0:	https://github.com/jnr/jnr-x86asm/archive/refs/tags/%{version}.tar.gz

BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Pure Java assembler for x86 and x86_64, used by jnr-ffi.

%prep
%setup -q -n jnr-x86asm-%{version}
# oss-parent 7 is a publishing parent. This project already has its license
# and compiler settings, and that parent POM is not installed.
sed -i '/<parent>/,/<\/parent>/d' pom.xml

%files -f .mfiles
%doc LICENSE README
