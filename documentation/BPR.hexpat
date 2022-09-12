// BALTIE PROGRAM FILE

#pragma endian little

struct Header{
	char file_magic[3];	// BPR Magic
	u8 version;			// Version (?)
	u16 tile_count;		// Amount of prgram blocks
};

struct Tile{			// Put it in a struct to have colorfull overlay
	u32 tile_data;		// Tile data (last 3 digits is tile number, rest is bank number)
};

// START

Header header @ 0x0;
Tile tiles[header.tile_count] @ 0x06;

