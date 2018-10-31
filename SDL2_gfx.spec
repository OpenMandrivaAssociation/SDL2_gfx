%define up_name   SDL2_gfx

%define major   0
%define apiver  1.0

%define libname     %mklibname %{name} %{apiver} %{major}
%define develname   %mklibname %{name} -d
%define develsname  %mklibname %{name} -d -s

Summary:    SDL2 graphics drawing primitives
Name:       sdl2_gfx
Version:    1.0.4
Release:    2
License:    ZLib
Group:      System/Libraries
URL:        http://www.ferzkopp.net/joomla/content/view/19/14/
Source0:    http://www.ferzkopp.net/Software/%{up_name}/%{up_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(sdl2)

%description
The SDL2_gfx library provides the basic drawing functions such
as lines, circles or polygons.
There is also an implementation of an interpolating rotozoomer for SDL2
surfaces.

The current components of the SDL2_gfx library are:

 * Graphic Primitives
 * Surface Rotozoomer
 * Framerate control
 * MMX image filters
 * Build-in 8x8 Font

%package -n   %{libname}
Summary:      Main library for %{name}
Group:        System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n   %{develname}
Summary:      Headers for developing programs that will use %{name}
Group:        Development/C
Requires:     %{libname} = %{version}-%{release}
Provides:     lib%{name}-devel = %{version}-%{release}
Provides:     %{name}%{apiver}-devel = %{version}-%{release}
Provides:     %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package      docs
Summary:      Documentation for %{up_name}
Group:        Documentation
BuildArch:    noarch

%description docs
This package contains the documentation for the %{up_name} library.

%prep
%setup -qn %{up_name}-%{version}
%apply_patches

%build
#autoreconf -vfi

%ifnarch %{ix86} x86_64
%configure2_5x --disable-mmx \
%else
%configure2_5x \
%endif
LIBS=-lm

%make_build

%install
%make_install

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/lib%{up_name}-%{apiver}.so.%{major}
%{_libdir}/lib%{up_name}-%{apiver}.so.%{major}.*

%files -n %{develname}
%doc README NEWS ChangeLog
%{_libdir}/lib%{up_name}.so
%{_libdir}/pkgconfig/%{up_name}.pc
%{_includedir}/SDL2/*

%files docs
%doc Docs/html
