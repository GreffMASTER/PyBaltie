// BALTIE PROGRAM FILE

#pragma endian little

struct header{
	char FileMagic[3];	// BPR Magic
	u8 Version;			// Version (?)
	u16 TileCount;		// Amount of prgram blocks
};

struct tile{			// Put it in a struct to have colorfull overlay
	u32 TileData;		// Tile data (last 3 digits is tile number, rest is bank number)
};

// START

header Header @ 0x0;
tile Tiles[Header.TileCount] @ 0x06;

