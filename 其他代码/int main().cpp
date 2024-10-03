int main()
{
    char str[300];
    while(scanf("%s",&str)!=EOF)
    {
        int i;
        for(i=0;str[i]!='\0';i++)
        {
            if(str[i]=='A')
                printf("T");
            else if(str[i]=='T')
                printf("A");
                else if(str[i]=='G')
                    printf("C");
                else if(str[i]=='C')
                    printf("G");
        }
        printf("\n");
    }
    return 0;
}
