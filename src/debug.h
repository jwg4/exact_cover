#ifndef DEBUG_LEVEL
#define DEBUG_LEVEL 0
#endif

#ifndef DEBUG_PRINT
#define DEBUG_PRINT(level, output) if (DEBUG_LEVEL >= level) fprintf(stderr, output);
#endif


