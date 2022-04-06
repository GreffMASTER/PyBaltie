struct fileheader{
	char FileMagic[4];
	u32 idk[12];
};

struct tileheader{
	le u8 TileStart[3];
	le u8 TrnsColor;
};

struct line{
	le u32 LineChunk1;
	le u8 L1;
	le u32 LineChunk2;
	le u8 L2;
	le u32 LineChunk3;
	le u8 L3;
	le u32 LineChunk4;
	le u8 L4;
};

struct tile{
	tileheader TileHeader;
	line Line[29];
	le u16 TileEnd;
};

// START

fileheader BankHeader @ 0x0;
tile Tile[1] @ 0x34;
