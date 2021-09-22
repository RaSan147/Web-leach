#include <stdio.h>
#include <string.h>
// #include <time.h>
#include <stdlib.h>
// #include <stdbool.h>
#define MAX_L 10000
#define MAX_keyL 10000

const char c_seq[96] =
	"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-*/.,\\<>?;':\"[]{}|_=`~!@#$%^&() ";
const short int seq[95][8] = {
		{ 5, 8, 1, 7, 2, 4, 3, 6 },
	{ 7, 2, 1, 6, 3, 8, 4, 5 },
	{ 3, 6, 2, 4, 7, 5, 1, 8 },
	{ 1, 8, 3, 6, 5, 7, 4, 2 },
	{ 2, 7, 8, 5, 4, 1, 3, 6 },
	{ 3, 4, 6, 8, 1, 2, 5, 7 },
	{ 2, 7, 4, 8, 3, 5, 6, 1 },
	{ 8, 6, 1, 5, 4, 2, 7, 3 },
	{ 4, 8, 1, 6, 3, 2, 5, 7 },
	{ 1, 7, 8, 2, 3, 4, 6, 5 },
	{ 1, 8, 3, 6, 2, 4, 7, 5 },
	{ 1, 4, 2, 8, 5, 3, 6, 7 },
	{ 5, 4, 7, 8, 3, 2, 1, 6 },
	{ 8, 2, 1, 4, 5, 6, 3, 7 },
	{ 6, 5, 4, 7, 1, 8, 3, 2 },
	{ 5, 8, 7, 1, 4, 2, 6, 3 },
	{ 2, 6, 4, 8, 1, 7, 3, 5 },
	{ 6, 3, 7, 5, 4, 1, 2, 8 },
	{ 4, 5, 7, 2, 6, 1, 3, 8 },
	{ 7, 3, 6, 5, 2, 1, 8, 4 },
	{ 3, 6, 4, 5, 1, 8, 2, 7 },
	{ 5, 1, 2, 8, 4, 7, 6, 3 },
	{ 6, 4, 2, 1, 7, 3, 5, 8 },
	{ 5, 7, 4, 2, 6, 3, 1, 8 },
	{ 7, 1, 2, 5, 6, 3, 8, 4 },
	{ 4, 8, 2, 1, 5, 7, 3, 6 },
	{ 3, 5, 8, 7, 1, 2, 6, 4 },
	{ 7, 5, 6, 8, 4, 2, 3, 1 },
	{ 7, 2, 1, 6, 5, 3, 8, 4 },
	{ 6, 3, 1, 8, 7, 5, 4, 2 },
	{ 3, 1, 5, 8, 7, 6, 4, 2 },
	{ 8, 3, 1, 5, 7, 4, 2, 6 },
	{ 7, 5, 8, 1, 3, 6, 2, 4 },
	{ 7, 5, 1, 8, 4, 3, 6, 2 },
	{ 7, 2, 3, 1, 6, 5, 4, 8 },
	{ 1, 2, 6, 4, 8, 7, 3, 5 },
	{ 7, 6, 2, 5, 4, 3, 8, 1 },
	{ 2, 8, 5, 3, 7, 6, 1, 4 },
	{ 4, 3, 5, 6, 2, 8, 7, 1 },
	{ 8, 1, 6, 2, 7, 5, 3, 4 },
	{ 4, 8, 3, 6, 1, 5, 2, 7 },
	{ 3, 4, 7, 6, 2, 8, 5, 1 },
	{ 4, 5, 8, 3, 6, 1, 2, 7 },
	{ 5, 4, 6, 2, 3, 7, 8, 1 },
	{ 7, 4, 3, 5, 1, 6, 8, 2 },
	{ 7, 4, 1, 5, 3, 8, 2, 6 },
	{ 5, 2, 8, 3, 7, 1, 4, 6 },
	{ 8, 2, 5, 6, 1, 7, 4, 3 },
	{ 7, 5, 1, 4, 3, 6, 8, 2 },
	{ 8, 5, 4, 6, 1, 3, 2, 7 },
	{ 6, 5, 7, 4, 8, 2, 1, 3 },
	{ 8, 3, 1, 7, 5, 4, 6, 2 },
	{ 2, 6, 7, 8, 4, 3, 1, 5 },
	{ 5, 2, 7, 8, 4, 3, 6, 1 },
	{ 4, 6, 8, 3, 1, 5, 7, 2 },
	{ 5, 1, 6, 3, 8, 7, 4, 2 },
	{ 7, 6, 3, 5, 1, 4, 2, 8 },
	{ 6, 8, 2, 7, 3, 4, 5, 1 },
	{ 7, 3, 5, 4, 6, 8, 1, 2 },
	{ 5, 8, 3, 7, 2, 4, 1, 6 },
	{ 7, 8, 6, 2, 1, 4, 5, 3 },
	{ 4, 8, 1, 3, 5, 2, 6, 7 },
	{ 8, 6, 7, 2, 5, 4, 3, 1 },
	{ 5, 8, 4, 2, 6, 3, 7, 1 },
	{ 4, 8, 7, 5, 2, 1, 3, 6 },
	{ 7, 1, 4, 2, 5, 8, 3, 6 },
	{ 2, 5, 1, 3, 7, 4, 6, 8 },
	{ 3, 7, 1, 4, 8, 2, 6, 5 },
	{ 7, 5, 6, 4, 8, 2, 3, 1 },
	{ 3, 8, 4, 7, 6, 2, 5, 1 },
	{ 4, 6, 3, 5, 8, 1, 2, 7 },
	{ 7, 2, 8, 4, 1, 3, 5, 6 },
	{ 4, 6, 7, 2, 1, 3, 8, 5 },
	{ 8, 2, 1, 5, 6, 4, 7, 3 },
	{ 6, 8, 5, 2, 4, 7, 3, 1 },
	{ 3, 7, 6, 8, 1, 5, 4, 2 },
	{ 3, 8, 1, 7, 5, 2, 6, 4 },
	{ 7, 2, 5, 6, 4, 3, 1, 8 },
	{ 3, 4, 1, 8, 2, 7, 5, 6 },
	{ 4, 7, 6, 2, 5, 1, 3, 8 },
	{ 6, 1, 3, 2, 5, 4, 7, 8 },
	{ 8, 4, 3, 5, 7, 2, 6, 1 },
	{ 3, 5, 6, 7, 1, 2, 8, 4 },
	{ 1, 3, 8, 6, 2, 7, 5, 4 },
	{ 5, 4, 1, 7, 6, 3, 8, 2 },
	{ 6, 3, 2, 1, 4, 5, 7, 8 },
	{ 3, 4, 5, 8, 7, 1, 2, 6 },
	{ 5, 6, 3, 8, 4, 2, 7, 1 },
	{ 7, 3, 4, 2, 5, 6, 8, 1 },
	{ 4, 6, 1, 3, 7, 2, 8, 5 },
	{ 1, 3, 6, 2, 8, 5, 7, 4 },
	{ 7, 1, 8, 5, 6, 4, 3, 2 },
	{ 3, 1, 5, 2, 8, 4, 6, 7 },
	{ 8, 5, 2, 4, 3, 1, 6, 7 },
	{ 2, 8, 7, 1, 4, 5, 3, 6 }
};

/*void swap(char *ptr1, char *ptr2)
	{
		char temp;
		temp = *ptr1;
		*ptr1 = *ptr2;
		*ptr2 = temp;
	}*/
/*int *indx(char *string, char *x){
	char *e;
	int *ind;
	e = strchr(string, x);
	ind =(int)(e - string);
	return ind;
} */

/*char *reverserx(char *str)
{
	int n = (int)strlen (str);
	char *x,*y;

	// Swap character starting from two

	// corners

	for (int i = 0; i < n / 2; i++) {
		swap(&str[n - i - 1],&str[n - i - 1]);
	}
	//printf("%s",str);
	//return str;
	return str;
}*/

/*int **reverser (char *dat)
{
	int i, j = 0;
	int len = strlen (dat);
	i = len - 1;
	char RevStr[MAX_L] = {};
	while (i >= 0)
		{
			RevStr[j] = dat[i];
			j++;
			i--;
		}
	RevStr[j] = '\0';
	strcpy (dat, RevStr);
	//printf("%s\n",data);
	return 0;
}*/

//gcc -c rcrypt1.c -I "D:\Ratul\Python Setup\include" -o rcrypt1.exe
//char *encrypt(char str
/*char *add_space (char *data)
{
	//printf("%s",data);
	unsigned int dat_len = strlen (data);
	//printf("%u", dat_len);
	if (dat_len % 8 != 0)
		{
			while (dat_len % 8 != 0)
	{
		data[dat_len] = '.';
		dat_len++;
	}
		}
	data[dat_len] = '\0';
	//printf("%s",data);
	return data;
}*/

int **
	reverser(char *dat)
	{
		int i, j = 0;
		unsigned int len = strlen(dat);
		i = len - 1;
		char RevStr[MAX_keyL] = {};
		while (i >= 0)
		{
			RevStr[j] = dat[i];
			j++;
			i--;
		}
		RevStr[j] = '\0';
		strcpy(dat, RevStr);
		//printf("%s\n",data);
		return 0;
	}

char *
	front2back_en(char *data, const int x, int dat_len)
	{
		//int a=0;
		//printf("%s",data);
		char front[8] = {};
		//while(a < 8){printf("f%cf",front[a]);a++;}
		int j = 0, i = 0;
		//printf(sizeof(front));
		while (i < x)
		{
			front[i] = data[i];
			i++;
		}
		//printf("%d\n",strlen(front));
		while (i < dat_len)
		{
			data[i - x] = data[i];
			i++;
		}
		while (j < x)
		{
			data[(i + j) - x] = front[j];
			j++;
		}
		return data;
	}

/*char *_encrypt (char *data, char c)
{
	char _back[9] = {};
	int _i = 0, _j, _x, _n, _loop, _ind;
	int _serial[8];
	for (_loop = 0; _loop < 8; _loop++)
		{
			// e = strchr(c_seq, c);
			_ind = (int) (strchr (c_seq, c) - c_seq);
			_serial[_loop] = seq[_ind][_loop];
		}
		int len=(int)strlen(data);

	while (_i < len)
		{
			_x = 0;
			_n = _i;
			while (_n < _i + 8)
	{
		_back[_x] = data[_n];
		_n++;
		_x++;
	}
			_x = 0;
			for (_j = 0; _j < 8; _j++)
	{
		data[_i + _x] = _back[_serial[_j] - 1];
		_x = (_x + 1) % 8;
	}

			_i += 8;
		}
	return data;
}*/

char *
	encrypt(char *data, char *key, long int msg_l, long int key_l)
	{
		char _back[9] = {};
		// char out[MAX_L];
		int _i, _j, _x, _n, _loop, _ind;
		int _serial[8];
		char _c;
		//printf(":%s:",data);
		// strcpy(data, out);
		if (msg_l % 8 != 0)
		{
			while (msg_l % 8 != 0)
			{
				data[msg_l] = ' ';
				msg_l++;
			}
		}
		data[msg_l] = '\0';
		//printf(":%s:",data);
		// data = add_space(data);
		unsigned int key_i = 0;
		// unsigned int dat_len= strlen(data);
		// unsigned int key_len= strlen(key);
		while (key_i < key_l)
		{
			_i = 0;
			// dat_i=0;
			front2back_en(data, 2, (int) msg_l);
			// printf(":%s:",data);
			// puts(data);
			/////_encrypt----start
			_c = key[key_i];
			// printf("--%d--\n",_c);
			_ind = (int)(strchr(c_seq, _c) - c_seq);
			for (_loop = 0; _loop < 8; _loop++)
			{
			 	// e = strchr(c_seq, c);
				_serial[_loop] = seq[_ind][_loop];
			}
			//      int len=(int)strlen(data);

			while (_i < msg_l)
			{
				_x = 0;
				_n = _i;
				while (_n < _i + 8)
				{
					_back[_x] = data[_n];
					_n++;
					_x++;
				}
				_x = 0;
				for (_j = 0; _j < 8; _j++)
				{
					data[_i + _x] = _back[_serial[_j] - 1];
					_x = (_x + 1) % 8;
				}

				_i += 8;
			}
			// puts(data);
			/////_encrypt----end
			key_i++;
			//printf("%d:%d\n",key_i, key_l);
		}
		//printf("%s",data);
		return data;
	}

char *
	b2f_de(char *data)
	{
		char front[MAX_L] = {};

		int x = 2, len = strlen(data), i = 0;
		while (i < len - x)
		{
			front[i] = data[i];
			i++;
		}
		//strncpy(front,data,(size_t)len-x);
		i = 0;
		while (i < x)
		{
			data[i] = data[len + i - x];
			i++;
		}
		i = 0;
		while (i < len - x)
		{
			data[i + x] = front[i];
			i++;
		}
		//int a=0;
		//printf("%s",data);
		//char rev_back[8]={};
		//while(a < 8){printf("f%cf",front[a]);a++;}
		//int b_step=0;
		//printf(sizeof(front));
		//while(b_step < x){
		//      rev_back[x-b_step-1]=data[len-b_step-1];
		//      b_step++;
		//}

		//reverser(rev_back);
		//strcat(front,rev_back);
		//printf("\n%s  %s\n",data,front);
		//strcpy(data,front);
		return data;
	}

char *
	_decrypt(char *data, char c)
	{

		char back[9] = {};
		int i = 0, j, x, n, loop;
		int serial[8];
		for (loop = 0; loop < 8; loop++)
		{
			int ind;
			// e = strchr(c_seq, c);
			ind = (int)(strchr(c_seq, c) - c_seq);
			serial[loop] = seq[ind][loop];
		}
		unsigned int len = strlen(data);

		while (i < (int) len)
		{
			x = 0;
			n = i;
			while (n < i + 8)
			{
				back[x] = data[n];
				n++;
				x++;
			}
			x = 0;
			// printf("==");
			for (j = 0; j < 8; j++)
			{
			 	// printf("%d",serial[j]);
				data[i + serial[j] - 1] = back[x];
				x++;
			}
			// printf("==");
			i += 8;
		}
		return data;
	}
char is_reversed =0;
char *
	decrypt(char *data, char *key, long int msg_l, long int key_l)
	{
		// int dat_i;
		//char _back[9] = {};
		// char out[MAX_L];
		int _serial[8];
		char _c;

		if (msg_l % 8 != 0)
		{
			while (msg_l % 8 != 0)
			{
				data[msg_l] = ' ';
				msg_l++;
			}
		}
		data[msg_l] = '\0';	// printf("\n1  %s",data);
		unsigned int key_i = 0;
		// unsigned int dat_len= strlen(data);
		unsigned int key_len = strlen(key);
		// printf("\n2  %s\t%s",data,key);
		if(is_reversed==0){
								reverser(key);
								is_reversed=1;
								}
		// printf("\n3  %s\t%s",data,key);
		while (key_i < key_len)
		{
			// dat_i=0;
			// printf("\n4  %s\t%s",data,key);
			_decrypt(data, key[key_i]);
			// printf("\n5  %s\t%s",data,key);
			b2f_de(data);
			key_i++;
		}
		return data;
	}

//lmlo wrR      dfro etoaul hl

char *
	returner(char *com, char *data, char *key, long int msg_l, unsigned int key_l)
	{
		// printf("%s",com);
		if (strcmp(com, "en") == 0)
		{
			data = encrypt(data, key, msg_l, key_l);
		}
		else
		{
			if (strcmp(com, "de") == 0)
			{
				data = decrypt(data, key, msg_l, key_l);
			}
			else
			{
				// data = decrypt(data, key, msg_l, key_l);
				                     printf("invalid input");
				                     exit (1);
			}
		}
		return data;
	}

int
main(int argc, char **argv)
{
    if(argc<2){
		printf("Invalid cmd arg!");
		exit(1);
	}
	//printf("hello madafakka c");
	// int count=0;
	// printf("'01'");
	char key[MAX_L];
	// printf("11");
	//char *out;

	// count=0;
	// printf ("Entered message!\n");
	//char input2[MAX_L] = {};
	//strcpy(input2, input);
	//printf("%s",input);
	//fgets (input, MAX_L, stdin);

	/*char *pos;
	   if ((pos = strchr (input, '\n')) != NULL)
	   *pos = '\0'; */

	FILE * fp;
	fp = fopen("k.txt", "r");
	if (fp == NULL)
	{
		printf("Error! opening k.txt file");
		exit(1);
	}
	int i = -1;
	//char arr[1000000];
	do {
		i++;
		key[i] = getc(fp);	// read character
		// putchar(key[i]);	// display character

	}
	while (key[i] != EOF);	// loop until the end of file is reached
	key[i] = '\0';
	fclose(fp);

	fp = fopen("out.txt", "w");
	//printf("%s",input);
	if (fp == NULL)
	{
		printf("Error! while writing output file");
		exit(1);
	}
	// printf ("Entered key!\n");

	//printf("%s",key);
	//fgets (key, MAX_L, stdin);
	//char *pos;
	//if ((pos = strchr (key, '\n')) != NULL)
	//      *pos = '\0';
	//char *inp = encrypt0(input);
	//char seq{100}{8};
	// printf("%s",input);
	double key_len = strlen(key);
	//clock_t en_begin = clock ();
	//printf("||%s||",input);

	char c[10000];
	char nxt[10001];
	char out[10000];
	FILE * fptr;
	if ((fptr = fopen("i.txt", "r")) == NULL)
	{
		printf("Error! opening i.txt file");
		// Program exits if file pointer returns NULL.
		exit(1);
	}

	// reads text until newline is encountered
	while (1)
	{
		nxt[0] = getc(fptr);
		nxt[1] = '\0';
		if (nxt[0] == EOF)
		{
			printf("End");
			fclose(fptr);
			break;
		}
		if (nxt[0] == '\n')
		{
			fprintf(fp, "\n");
		}
		else
		{

			fscanf(fptr, "%[^\n]", c);
			strcat(nxt, c);
			// printf("%s", c);
			// printf("\"%s\"\n\n\"%s\"\n\n", nxt, key);

			returner(argv[1], nxt, key, strlen(nxt), key_len);

			// printf("\"%s\"\n\n\"%s\"\n\n", nxt, key);

			fprintf(fp, "%s", nxt);
		}

		*out = '\0';
		*nxt = '\0';
		*c = '\0';
	}
	//clock_t en_end = clock
	//printf("bye");

	//double en_time_spent = (double) (en_end - en_begin) / CLOCKS_PER_SEC;
	//printf ("encrypted\n=========\n\n%s\n\nEncrypted in %fs", light, en_time_spent);
	//char aaa[]="qwert";
	//reverser(&aaa);
	//printf("%s",aaa); */
	//clock_t de_begin = clock ();
	//printf("%s%s", argv[1],input);
	//clock_t de_end = clock ();
	//double de_time_spent = (double) (de_end - de_begin) / CLOCKS_PER_SEC;
	//printf ("\ndecrypted\n=========\n\n%s\n\nDecrypted in %fs\n", dark, de_time_spent);
	/*printf
	   ("Msg len= %d\nKey len= %d\n\nEncrypted in %lfs\nDecrypted in %lfs\n time per key (en): %lfs\n       time per key (de): %lfs",
	   (int) msg_len, (int) key_len, en_time_spent, de_time_spent,
	   (double) (en_time_spent / key_len), (double) (de_time_spent / key_len)); */

	//printf("Enter num: ");
	//scanf("%d",&num);
	fclose(fp);

	return 0;
}