class MyCalendarTwo {
    map<int,int> mp;

public:
    MyCalendarTwo() {
        
    }
    
    bool book(int s, int e) {
        mp[s]++;     // event starts here, so +1 booking
        mp[e]--;     // event ends here, so -1 booking

        int prefix = 0;

        for (auto &[key, value] : mp) {
            prefix += value;   // current active bookings

            if (prefix == 3) { // triple booking found
                mp[s]--;       // rollback start
                mp[e]++;       // rollback end
                return false;
            }
        }

        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(startTime,endTime);
 */