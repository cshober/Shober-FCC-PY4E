#include <iostream>
#include <string>
using namespace std;

int split(string str, char lim, string arr[], int size){
    if (str == "") //if the string is empty return 0
        return 0;

    string word = ""; //create variable to hold each word
    str += lim; //add delimiter to end of the string so the prgram knows when the last word ends
    int count = 0; //create counter to hold number of elements
    for (int i = 0; i < str.length(); i++) //for loop that runs through each charcter of string
    {
        if (str[i] == lim && word != "") //if the string at index is the delimiter or the word is empty (2 delimters in a row)
        {
            arr[count] = word; //set the array at current count to the string stored in word variable
            count++; //add 1 to the number of elements
            word = ""; //reset the word variable to empty to store the next word
            if (count > size) //check to see the size is still in bounds to prevent seg fault
            {
                return -1;
            }
        }
        else if (str[i] != lim) //if the delimter is not reached
        {
            word += str[i]; //add character at indx to the word variable
        }
    }
    return count; //return number of elements
}