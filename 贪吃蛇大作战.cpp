#include<iostream> 
#include<windows.h> 
#include<conio.h> 
#include<time.h> 
#include<stdlib.h> 
using namespace std; 
const int N=21;
const int A=21;
void Get_xy(int x,int y) //定位光标位置 
{ 
    HANDLE hout; 
    COORD pos; 
    pos.X=x*2; 
    pos.Y=y; 
    hout=GetStdHandle(STD_OUTPUT_HANDLE); 
    SetConsoleCursorPosition(hout,pos); 
} 

void Color(int num) //设置颜色 
{ 
    HANDLE hout; 
    hout=GetStdHandle(STD_OUTPUT_HANDLE); 
    SetConsoleTextAttribute(hout,num); 
} 
int jc1;
int jc2;
void Initial() //初始化 
{ 
    int i,j;
    int wall[N+2][N+2]={{0}}; 
    for(i=1;i<=N;i++) 
    for(j=1;j<=N;j++) 
    wall[i][j]=1; 
    Color(11); 
    for(i=0;i<N+2;i++) 
    { 
        for(j=0;j<N+2;j++) 
        { 
            if(wall[i][j]) 
            cout<<"■"; 
            else
		    cout<<"□"; 
        } 
        cout<<endl; 
    } 
    Get_xy(N+3,1); Color(20); 
    cout<<"按'W','S','A','D'进行操作"<<endl; 
    Get_xy(N+3,2); Color(20); 
    cout<<"按任意键暂停"<<endl; 
    Get_xy(N+3,3); Color(20); 
    cout<<"得分："<<endl; 
} 
void game() 
{ 
    int** snake=NULL; 
    int** snake2=NULL;
    int len=1; 
    int len2=1; 
    int i;
    int i2;
    int score=0; 
    int score2=0;
    int apple[2][A]; 
    int tail[2]; 
    int tail2[2]; 
    
    char ch='p'; 
    Initial(); 
    
    srand((unsigned)time(NULL)); 
	for(i=1;i<=A;i++)
	{
	    apple[0][i]=rand()%N+1; 
	    apple[1][i]=rand()%N+1; 
	    Get_xy(apple[0][i],apple[1][i]); 
    	Color(12); 
   		cout<<"●"<<endl; 
	}
	
    snake=(int**)realloc(snake,sizeof(int*)*len); 
    for(i=0;i<len;i++) 
    snake[i]=(int*)malloc(sizeof(int)*2); 
    snake[0][0]=N/4*3; 
    snake[0][1]=N/2+1; 
    Get_xy(snake[0][0],snake[0][1]); Color(14); 
    cout<<"⊙"<<endl;
    
    int flag=1;
    
    snake2=(int**)realloc(snake2,sizeof(int*)*len2);
    for(i2=0;i2<len2;i2++) 
    snake2[i2]=(int*)malloc(sizeof(int)*2); 
    snake2[0][0]=N/4; 
    snake2[0][1]=N/2+1; 
    Get_xy(snake2[0][0],snake2[0][1]); Color(15); 
    cout<<"⊙"<<endl;
	 
    int flag2=1;
    
    while(1) 
    { 
        if(flag) 
        { 
            tail[0]=snake[len-1][0]; 
            tail[1]=snake[len-1][1]; 
            Get_xy(tail[0],tail[1]); 
            Color(11); 
            cout<<"■"<<endl; 
        } 
        flag=1; 
        for(i=len-1;i>0;i--) 
        { 
            snake[i][0]=snake[i-1][0]; 
            snake[i][1]=snake[i-1][1]; 
            Get_xy(snake[i][0],snake[i][1]); 
            Color(14); 
            cout<<"卐"<<endl; 
        } 
        
        if(flag2) 
        { 
            tail2[0]=snake2[len2-1][0]; 
            tail2[1]=snake2[len2-1][1]; 
            Get_xy(tail2[0],tail2[1]); 
            Color(11); 
            cout<<"■"<<endl; 
        } 
        flag2=1; 
        for(i=len2-1;i>0;i--) 
        { 
            snake2[i][0]=snake2[i-1][0]; 
            snake2[i][1]=snake2[i-1][1]; 
            Get_xy(snake2[i][0],snake2[i][1]); 
            Color(15); 
            cout<<"卐"<<endl; 
        } 
        
        if(kbhit()) 
        { 
            Get_xy(0,N+3); 
            ch=getche(); 
        } 
        
        switch(ch) 
        { 
        case 'W': 
        case 'w':jc1=1;
		break; 
        case 'S': 
        case 's': jc1=2;
        break; 
        case 'A': 
        case 'a': jc1=3;
        break; 
        case 'D': 
        case 'd': jc1=4;
        break; 
    	}
    	
    	if(kbhit()) 
        { 
            Get_xy(0,N+3); 
            ch=getche(); 
        } 
    	switch(ch)
    	{
        case '5': jc2=1;
		break;  
        case '2': jc2=2;
        break; 
        case '1': jc2=3;
        break; 
        case '3': jc2=4;
        break; 
        
        default :break; 
        } 
        
        if(jc1==1)snake[0][1]--; 
        if(jc1==2)snake[0][1]++; 
        if(jc1==3)snake[0][0]--; 
        if(jc1==4)snake[0][0]++;
        
        if(jc2==1)snake2[0][1]--; 
        if(jc2==2)snake2[0][1]++; 
        if(jc2==3)snake2[0][0]--; 
        if(jc2==4)snake2[0][0]++;
        
        for(i=1;i<len;i++) 
        { 
            if(snake[0][0]==snake[i][0] && snake[0][1]==snake[i][1]) 
            { 
                Get_xy(N/2,N/2); Color(30); 
                cout<<"snake2 win"<<endl; 
                exit(0); 
            } 
            if(snake2[0][0]==snake[i][0] && snake2[0][1]==snake[i][1])
            {
            	Get_xy(N/2,N/2); Color(30); 
                cout<<"snake1 win"<<endl; 
                exit(0); 
			}
        } 
        Get_xy(snake[0][0],snake[0][1]); 
        Color(14); cout<<"⊙"<<endl; 
         
        for(i=1;i<len2;i++) 
        { 
            if(snake2[0][0]==snake2[i][0] && snake2[0][1]==snake2[i][1]) 
            { 
                Get_xy(N/2,N/2); Color(30); 
                cout<<"snake1 win"<<endl; 
                exit(0); 
            } 
            if(snake[0][0]==snake2[i][0] && snake[0][1]==snake2[i][1])
            {
            	Get_xy(N/2,N/2); Color(30); 
                cout<<"snake2 win"<<endl; 
                exit(0); 
			}
        } 
        
        Get_xy(snake2[0][0],snake2[0][1]); 
        Color(15); cout<<"⊙"<<endl; 
        Sleep(200); 
        for(int i=1;i<=A;i++)
        {
        	if(snake[0][0]==apple[0][i] && snake[0][1]==apple[1][i]) 
	        { 
	            flag=0;
				score++;
			    len++; 
				srand((unsigned)time(NULL)); 
	            snake=(int**)realloc(snake,sizeof(int*)*len); 
	            snake[len-1]=(int*)malloc(sizeof(int)*2); 
	            Get_xy(N+6,3); Color(20); cout<<score<<endl; 
	            apple[0][i]=rand()%N+1; apple[1][i]=rand()%N+1; 
	            Get_xy(apple[0][i],apple[1][i]); 
	            Color(12); 
	            cout<<"●"<<endl; 
	        } 
	        
	        if(snake2[0][0]==apple[0][i] && snake2[0][1]==apple[1][i]) 
	        { 
	            flag2=0;
				score2++;
			    len2++; 
				srand((unsigned)time(NULL)); 
	            snake2=(int**)realloc(snake2,sizeof(int*)*len2); 
	            snake2[len2-1]=(int*)malloc(sizeof(int)*2); 
	            Get_xy(N+6,3); Color(20); cout<<score2<<endl; 
	            apple[0][i]=rand()%N+1; apple[1][i]=rand()%N+1; 
	            Get_xy(apple[0][i],apple[1][i]); 
	            Color(12); 
	            cout<<"●"<<endl; 
	        }
		} 
        
        if(snake[0][0]==-1 || snake[0][0]==N+1 || snake[0][1]==-1 || snake[0][1]==N+1) 
        { 
            Get_xy(N/2,N/2); Color(30); 
            cout<<"snake2 win"<<endl; 
            for(int i=0;i<len;i++) 
            free(snake[i]); 
            Sleep(INFINITE); 
            exit(0); 
        } 
        if(snake2[0][0]==-1 || snake2[0][0]==N+1 || snake2[0][1]==-1 || snake2[0][1]==N+1) 
        { 
            Get_xy(N/2,N/2); Color(30); 
            cout<<"snake1 win"<<endl; 
            for(int i=0;i<len2;i++) 
            free(snake2[i]); 
            Sleep(INFINITE); 
            exit(0); 
        } 
//        if(len>=N*N-1) 
//        { 
//            Get_xy(N/2,N/2); Color(30); 
//            cout<<"win!"<<endl; 
//            for(i=0;i<len;i++) 
//            free(snake[i]); 
//            Sleep(INFINITE); 
//            exit(0); 
//        } 
    } 
} 
int main() 
{ 
game(); 
}
