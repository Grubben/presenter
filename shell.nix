with import <nixpkgs> {};

stdenv.mkDerivation {
	name = "openage-env";
	version = "0.1";

	nativeBuildInputs = [ python3 ];
	buildInputs = [
		python39Packages.tkinter
		python39Packages.pygame
	];

	shellHook = ''
		source ~/.bash_profile
		python3 --version
		echo "hello, world"
	'';
}
