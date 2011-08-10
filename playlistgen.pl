#!/usr/bin/perl -w
#
# Author: Sai Charan (http://saicharan.in/blog)
# Distributed without warranties or conditions of any kind, either
# express or implied except those under the CC BY-NC 3.0 license. 
# You may obtain a copy of the license at:
#
# http://creativecommons.org/licenses/by-nc/3.0/
#
# Author: Sai Charan K (http://saicharan.in/blog)
# Date: 5th March 2010
#
# M3U Playlist generator.
#
# Run this script on any top level directory and you will have a .m3u file for each
# directory/sub directory that contains one or more mp3 files.
# You can choose to support multiple audio file formats by modifying the 
# audioFileExtensions variable.
#
# Note(s) to self:
# - The list of supported files can be moved to a .rc file or passed as args.
#
# Version history
# v0.1: Initial draft, 5th march 2010.
# v0.2: Completed initial version, 9th march 2010.

use warnings;
use strict;
use File::Find;

# Add more extensions here: for example, to allow wma files,
# the new regular expression will be "\.(mp3|wma)\$"
my $audioFileExtensions = "\.(mp3)\$";	

my @fileList = ();
my @dirList = ();

sub worker($){
	push @dirList, $File::Find::name if -d;
}

sub createPlaylist($){
	#create a playlist ONLY if there is atleast ONE audio file.
	return unless (scalar(@fileList) > 0);
	my $dir = (shift);
	
	#Name the playlist file as playlist.m3u
	my $playlistFileName = $dir."/playlist.m3u";
	open my $playlistFileHandle, ">$playlistFileName" or die("Could not create playlist file: $dir/playlist.m3u");
	
	#print header.
	printf $playlistFileHandle "#EXTM3U\n";
	foreach my $mp3File (@fileList){
		printf $playlistFileHandle "#EXTINF:0,$mp3File\n";
		printf $playlistFileHandle $mp3File."\n\n";
	}
	close ($playlistFileHandle);
	
	@fileList = ();
}

sub main(){
	#can do better: take directory to process as argument.
    find( \&worker, '.');
	foreach my $dir ( @dirList ){
		@fileList = ();
		opendir(DIR, $dir);
		@fileList = grep( /$audioFileExtensions/i, readdir(DIR) );
		closedir(DIR);
		createPlaylist($dir);
	}
}

#Main entry point
main();
