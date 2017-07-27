#!/bin/bash
cd /pango-install/

# Install libffi
# echo 'Obtaining libffi'
# wget ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
# tar -xf libffi-3.2.1.tar.gz
# cd libffi-3.2.1
#
# echo 'Configuring libffi'
# sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' \
#     -i include/Makefile.in &&
#
# sed -e '/^includedir/ s/=.*$/=@includedir@/' \
#     -e 's/^Cflags: -I${includedir}/Cflags:/' \
#     -i libffi.pc.in        &&
#
# ./configure --prefix=/usr --disable-static &&
# make
#
# echo 'Installing libffi'
# make install
# cd ..

# Install Bzip2
# echo 'Obtaining Bzip2'
# wget ftp://sources.redhat.com/pub/bzip2/v102/bzip2-1.0.2.tar.gz
# tar -xf bzip2-1.0.2.tar.gz
# cd bzip2-1.0.2
#
# echo 'Configuring Bzip2'
# make -f Makefile-libbz2_so
# make clean
# make
#
# echo 'Installing Bzip2'
# make PREFIX=/usr install
# cp -v bzip2-shared /bin/bzip2
# cp -av libbz2.so* /lib
# ln -sv ../../lib/libbz2.so.1.0 /usr/lib/libbz2.so
# rm -v /usr/bin/{bunzip2,bzcat,bzip2}
# ln -sv bzip2 /bin/bunzip2
# ln -sv bzip2 /bin/bzcat
# cd ..

# Install ncurses
# echo 'Obtaining ncurses'
# wget ftp://ftp.gnu.org/gnu/ncurses/ncurses-6.0.tar.gz
# tar -xf ncurses-6.0.tar.gz
# cd ncurses-6.0
#
# echo 'Configuring ncurses'
# sed -i '/LIBTOOL_INSTALL/d' c++/Makefile.in
# ./configure --prefix=/usr \
#             --mandir=/usr/share/man \
#             --with-shared \
#             --without-debug \
#             --without-normal \
#             --enable-pc-files \
#             --enable-widec
# make
#
# echo 'Installing ncurses'
# make install
# mv -v /usr/lib/libncursesw.so.6* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libncursesw.so) /usr/lib/libncursesw.so
# for lib in ncurses form panel menu ; do
#     rm -vf                    /usr/lib/lib${lib}.so
#     echo "INPUT(-l${lib}w)" > /usr/lib/lib${lib}.so
#     ln -sfv ${lib}w.pc        /usr/lib/pkgconfig/${lib}.pc
# done
# rm -vf /usr/lib/libcursesw.so
# echo "INPUT(-lncursesw)" > /usr/lib/libcursesw.so
# ln -sfv libncurses.so /usr/lib/libcurses.so
# cd ..

# Install readline
# echo 'Obtaining readline'
# wget http://ftp.gnu.org/gnu/readline/readline-7.0.tar.gz
# tar -xf readline-7.0.tar.gz
# cd readline-7.0
#
# echo 'Configuring readline'
# sed -i '/MV.*old/d' Makefile.in
# sed -i '/{OLDSUFF}/c:' support/shlib-install
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/readline-7.0
# make SHLIB_LIBS="-L/tools/lib -lncursesw"
#
# echo 'Installing readline'
# make SHLIB_LIBS="-L/tools/lib -lncurses" install
# mv -v /usr/lib/lib{readline,history}.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libreadline.so) /usr/lib/libreadline.so
# ln -sfv ../../lib/$(readlink /usr/lib/libhistory.so ) /usr/lib/libhistory.so
# cd ..

# Install PCRE
# echo 'Obtaining PCRE'
# wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.41.tar.bz2
# tar -xf pcre-8.41.tar.bz2
# cd pcre-8.41
#
# echo 'Configuring PCRE'
# ./configure --prefix=/usr \
#             --docdir=/usr/share/doc/pcre-8.41 \
#             --enable-unicode-properties \
#             --enable-pcre16 \
#             --enable-pcre32 \
#             --enable-pcregrep-libz \
#             --enable-pcregrep-libbz2 \
#             --enable-pcretest-libreadline \
#             --disable-static &&
# make
#
# echo 'Installing PCRE'
# make install &&
# mv -v /usr/lib/libpcre.so.* /lib &&
# ln -sfv ../../lib/$(readlink /usr/lib/libpcre.so) /usr/lib/libpcre.so
# cd ..

# Install gettext
# echo 'Obtaining gettext'
# wget http://ftp.gnu.org/pub/gnu/gettext/gettext-0.19.8.tar.gz
# tar -xf gettext-0.19.8.tar.gz
# cd gettext-0.19.8
#
# echo 'Configuring getext'
# sed -i '/^TESTS =/d' gettext-runtime/tests/Makefile.in &&
# sed -i 's/test-lock..EXEEXT.//' gettext-tools/gnulib-tests/Makefile.in
#
# ./configure --prefix=/usr    \
#             --disable-static
# make
#
# echo 'Installing gettext'
# make install
# cd ..

# Install util-linux (for libmount)
# echo 'Obtaining util-linux'
# wget https://www.kernel.org/pub/linux/utils/util-linux/v2.30/util-linux-2.30.1.tar.gz
# tar -xf util-linux-2.30.1.tar.gz
# cd util-linux-2.30.1
#
# echo 'Configuring util-linux'
# mkdir -pv /var/lib/hwclock
# ./configure ADJTIME_PATH=/var/lib/hwclock/adjtime \
#             --docdir=/usr/share/doc/util-linux-2.30.1 \
#             --disable-chfn-chsh \
#             --disable-login \
#             --disable-nologin \
#             --disable-su \
#             --disable-setpriv \
#             --disable-runuser \
#             --disable-pylibmount \
#             --disable-static \
#             --without-python \
#             --without-systemd \
#             --without-systemdsystemunitdir
# make
#
# echo "Installing util-linux"
# make install
# cd ..

# Install GLib
# echo 'Obtaining GLib'
# wget ftp://ftp.gnome.org/pub/gnome/sources/glib/2.52/glib-2.52.3.tar.xz
# tar -xf glib-2.52.3.tar.xz
# cd glib-2.52.3
#
# echo 'Configuring GLib'
# ./configure --prefix=/usr --with-pcre=system &&
# make
#
# echo 'Installing GLib'
# make install
# cd ..

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

# Install ICU-59.1
# echo 'Obtaining ICU'
# wget http://download.icu-project.org/files/icu4c/59.1/icu4c-59_1-src.tgz
# tar -xf icu4c-59_1-src.tgz
# cd icu
#
# echo 'Configuring ICU'
# cd source &&
# ./configure --prefix=/usr &&
# make
#
# echo 'Installing ICU'
# make install
# cd ../..

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
