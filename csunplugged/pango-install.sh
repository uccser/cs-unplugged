#!/bin/bash
cd /pango-install/

# Install libpng
echo 'Obtaining libpng'
wget http://downloads.sourceforge.net/libpng/libpng-1.6.29.tar.xz
tar -xf libpng-1.6.29.tar.xz
cd libpng-1.6.29

echo 'Configuring libpng'
LIBS=-lpthread ./configure --prefix=/usr --disable-static &&
make

echo 'Installing libpng'
make install &&
mkdir -v /usr/share/doc/libpng-1.6.29 &&
cp -v README libpng-manual.txt /usr/share/doc/libpng-1.6.29
cd ..

# Install Which
echo 'Obtaining Which'
wget ftp://ftp.gnu.org/gnu/which/which-2.21.tar.gz
tar -xf which-2.21.tar.gz
cd which-2.21

echo 'Configuring Which'
./configure --prefix=/usr &&
make

echo 'Installing Which'
make install
cd ..

# Install FreeType
echo 'Obtaining FreeType'
wget http://downloads.sourceforge.net/freetype/freetype-2.8.tar.bz2
tar -xf freetype-2.8.tar.bz2
cd freetype-2.8

echo 'Configuring FreeType'
sed -ri "s:.*(AUX_MODULES.*valid):\1:" modules.cfg &&
sed -r "s:.*(#.*SUBPIXEL_RENDERING) .*:\1:" \
    -i include/freetype/config/ftoption.h  &&
./configure --prefix=/usr --disable-static &&
make

echo 'Installing FreeType'
make install &&
install -v -m755 -d /usr/share/doc/freetype-2.8 &&
cp -v -R docs/*     /usr/share/doc/freetype-2.8
cd ..

# Install HarfBuzz with FreeType2
echo 'Obtaining HarfBuzz'
wget http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.4.6.tar.bz2
tar -xf harfbuzz-1.4.6.tar.bz2
cd harfbuzz-1.4.6

echo 'Configuring HarfBuzz'
./configure --prefix=/usr --with-gobject &&
make

echo 'Installing HarfBuzz'
make install
cd ..

# Reinstall FreeType2 with HarfBuzz support
echo 'Reinstalling FreeType2'
cd freetype-2.8
./configure --prefix=/usr --disable-static &&
make &&
make install &&
install -v -m755 -d /usr/share/doc/freetype-2.8 &&
cp -v -R docs/*     /usr/share/doc/freetype-2.8
cd ..

# Install Fontconfig-2
echo 'Obtaining Fontconfig'
wget http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.12.4.tar.bz2
tar -xf fontconfig-2.12.4.tar.bz2
cd fontconfig-2.12.4

echo 'Configuring Fontconfig'
rm -f src/fcobjshash.h
./configure --prefix=/usr \
            --sysconfdir=/etc \
            --localstatedir=/var \
            --disable-docs \
            --docdir=/usr/share/doc/fontconfig-2.12.4 &&
make

echo 'Installing Fontconfig'
make install
cd ..

# install Pango-1.40
echo 'Obtaining Pango'
wget ftp://ftp.gnome.org/pub/gnome/sources/pango/1.40/pango-1.40.6.tar.xz
tar -xf pango-1.40.6.tar.xz
cd pango-1.40.6

echo 'Configuring Pango'
./configure --prefix=/usr --sysconfdir=/etc &&
make

echo 'Installing Pango'
make install

cd /
