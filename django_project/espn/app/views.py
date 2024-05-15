
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    json_data = [
    {
        "M_no": "1st Match, (N) at Chennai, Mar 22 2024",
        "vs": "(RCB vs CSK)",
        "result": "CSK won by 6 wkts (8b rem)"
    },
    {
        "M_no": "2nd Match, (D/N) at Mohali, Mar 23 2024",
        "vs": "(DC vs PBKS)",
        "result": "PBKS won by 4 wkts (4b rem)"
    },
    {
        "M_no": "3rd Match, (N) at Kolkata, Mar 23 2024",
        "vs": "(SRH vs KKR)",
        "result": "KKR won by 4 runs"
    },
    {
        "M_no": "4th Match, (D/N) at Jaipur, Mar 24 2024",
        "vs": "(LSG vs RR)",
        "result": "RR won by 20 runs"
    },
    {
        "M_no": "5th Match, (N) at Ahmedabad, Mar 24 2024",
        "vs": "(MI vs GT)",
        "result": "GT won by 6 runs"
    },
    {
        "M_no": "6th Match, (N) at Bengaluru, Mar 25 2024",
        "vs": "(PBKS vs RCB)",
        "result": "RCB won by 4 wkts (4b rem)"
    },
    {
        "M_no": "7th Match, (N) at Chennai, Mar 26 2024",
        "vs": "(GT vs CSK)",
        "result": "CSK won by 63 runs"
    },
    {
        "M_no": "8th Match, (N) at Hyderabad, Mar 27 2024",
        "vs": "(MI vs SRH)",
        "result": "SRH won by 31 runs"
    },
    {
        "M_no": "9th Match, (N) at Jaipur, Mar 28 2024",
        "vs": "(DC vs RR)",
        "result": "RR won by 12 runs"
    },
    {
        "M_no": "10th Match, (N) at Bengaluru, Mar 29 2024",
        "vs": "(KKR vs RCB)",
        "result": "KKR won by 7 wkts (19b rem)"
    },
    {
        "M_no": "11th Match, (N) at Lucknow, Mar 30 2024",
        "vs": "(PBKS vs LSG)",
        "result": "LSG won by 21 runs"
    },
    {
        "M_no": "12th Match, (D/N) at Ahmedabad, Mar 31 2024",
        "vs": "(SRH vs GT)",
        "result": "GT won by 7 wkts (5b rem)"
    },
    {
        "M_no": "13th Match, (N) at Visakhapatnam, Mar 31 2024",
        "vs": "(CSK vs DC)",
        "result": "DC won by 20 runs"
    },
    {
        "M_no": "14th Match, (N) at Mumbai, Apr 1 2024",
        "vs": "(RR vs MI)",
        "result": "RR won by 6 wkts (27b rem)"
    },
    {
        "M_no": "15th Match, (N) at Bengaluru, Apr 2 2024",
        "vs": "(LSG vs RCB)",
        "result": "LSG won by 28 runs"
    },
    {
        "M_no": "16th Match, (N) at Visakhapatnam, Apr 3 2024",
        "vs": "(KKR vs DC)",
        "result": "KKR won by 106 runs"
    },
    {
        "M_no": "17th Match, (N) at Ahmedabad, Apr 4 2024",
        "vs": "(PBKS vs GT)",
        "result": "PBKS won by 3 wkts (1b rem)"
    },
    {
        "M_no": "18th Match, (N) at Hyderabad, Apr 5 2024",
        "vs": "(CSK vs SRH)",
        "result": "SRH won by 6 wkts (11b rem)"
    },
    {
        "M_no": "19th Match, (N) at Jaipur, Apr 6 2024",
        "vs": "(RCB vs RR)",
        "result": "RR won by 6 wkts (5b rem)"
    },
    {
        "M_no": "20th Match, (D/N) at Mumbai, Apr 7 2024",
        "vs": "(DC vs MI)",
        "result": "MI won by 29 runs"
    },
    {
        "M_no": "21st Match, (N) at Lucknow, Apr 7 2024",
        "vs": "(GT vs LSG)",
        "result": "LSG won by 33 runs"
    },
    {
        "M_no": "22nd Match, (N) at Chennai, Apr 8 2024",
        "vs": "(KKR vs CSK)",
        "result": "CSK won by 7 wkts (14b rem)"
    },
    {
        "M_no": "23rd Match, (N) at Mohali, Apr 9 2024",
        "vs": "(SRH vs PBKS)",
        "result": "SRH won by 2 runs"
    },
    {
        "M_no": "24th Match, (N) at Jaipur, Apr 10 2024",
        "vs": "(GT vs RR)",
        "result": "GT won by 3 wkts (0b rem)"
    },
    {
        "M_no": "25th Match, (N) at Mumbai, Apr 11 2024",
        "vs": "(RCB vs MI)",
        "result": "MI won by 7 wkts (27b rem)"
    },
    {
        "M_no": "26th Match, (N) at Lucknow, Apr 12 2024",
        "vs": "(DC vs LSG)",
        "result": "DC won by 6 wkts (11b rem)"
    },
    {
        "M_no": "27th Match, (N) at Mohali, Apr 13 2024",
        "vs": "(RR vs PBKS)",
        "result": "RR won by 3 wkts (1b rem)"
    },
    {
        "M_no": "28th Match, (D/N) at Kolkata, Apr 14 2024",
        "vs": "(LSG vs KKR)",
        "result": "KKR won by 8 wkts (26b rem)"
    },
    {
        "M_no": "29th Match, (N) at Mumbai, Apr 14 2024",
        "vs": "(CSK vs MI)",
        "result": "CSK won by 20 runs"
    },
    {
        "M_no": "30th Match, (N) at Bengaluru, Apr 15 2024",
        "vs": "(SRH vs RCB)",
        "result": "SRH won by 25 runs"
    },
    {
        "M_no": "31st Match, (N) at Kolkata, Apr 16 2024",
        "vs": "(RR vs KKR)",
        "result": "RR won by 2 wkts (0b rem)"
    },
    {
        "M_no": "32nd Match, (N) at Ahmedabad, Apr 17 2024",
        "vs": "(DC vs GT)",
        "result": "DC won by 6 wkts (67b rem)"
    },
    {
        "M_no": "33rd Match, (N) at Mohali, Apr 18 2024",
        "vs": "(MI vs PBKS)",
        "result": "MI won by 9 runs"
    },
    {
        "M_no": "34th Match, (N) at Lucknow, Apr 19 2024",
        "vs": "(CSK vs LSG)",
        "result": "LSG won by 8 wkts (6b rem)"
    },
    {
        "M_no": "35th Match, (N) at Delhi, Apr 20 2024",
        "vs": "(SRH vs DC)",
        "result": "SRH won by 67 runs"
    },
    {
        "M_no": "36th Match, (D/N) at Kolkata, Apr 21 2024",
        "vs": "(RCB vs KKR)",
        "result": "KKR won by 1 run"
    },
    {
        "M_no": "37th Match, (N) at Mohali, Apr 21 2024",
        "vs": "(GT vs PBKS)",
        "result": "GT won by 3 wkts (5b rem)"
    },
    {
        "M_no": "38th Match, (N) at Jaipur, Apr 22 2024",
        "vs": "(MI vs RR)",
        "result": "RR won by 9 wkts (8b rem)"
    },
    {
        "M_no": "39th Match, (N) at Chennai, Apr 23 2024",
        "vs": "(LSG vs CSK)",
        "result": "LSG won by 6 wkts (3b rem)"
    },
    {
        "M_no": "40th Match, (N) at Delhi, Apr 24 2024",
        "vs": "(GT vs DC)",
        "result": "DC won by 4 runs"
    },
    {
        "M_no": "41st Match, (N) at Hyderabad, Apr 25 2024",
        "vs": "(RCB vs SRH)",
        "result": "RCB won by 35 runs"
    },
    {
        "M_no": "42nd Match, (N) at Kolkata, Apr 26 2024",
        "vs": "(PBKS vs KKR)",
        "result": "PBKS won by 8 wkts (8b rem)"
    },
    {
        "M_no": "43rd Match, (D/N) at Delhi, Apr 27 2024",
        "vs": "(MI vs DC)",
        "result": "DC won by 10 runs"
    },
    {
        "M_no": "44th Match, (N) at Lucknow, Apr 27 2024",
        "vs": "(RR vs LSG)",
        "result": "RR won by 7 wkts (6b rem)"
    },
    {
        "M_no": "45th Match, (D/N) at Ahmedabad, Apr 28 2024",
        "vs": "(RCB vs GT)",
        "result": "RCB won by 9 wkts (24b rem)"
    },
    {
        "M_no": "46th Match, (N) at Chennai, Apr 28 2024",
        "vs": "(SRH vs CSK)",
        "result": "CSK won by 78 runs"
    },
    {
        "M_no": "47th Match, (N) at Kolkata, Apr 29 2024",
        "vs": "(DC vs KKR)",
        "result": "KKR won by 7 wkts (21b rem)"
    },
    {
        "M_no": "48th Match, (N) at Lucknow, Apr 30 2024",
        "vs": "(MI vs LSG)",
        "result": "LSG won by 4 wkts (4b rem)"
    },
    {
        "M_no": "49th Match, (N) at Chennai, May 1 2024",
        "vs": "(PBKS vs CSK)",
        "result": "PBKS won by 7 wkts (13b rem)"
    },
    {
        "M_no": "50th Match, (N) at Hyderabad, May 2 2024",
        "vs": "(RR vs SRH)",
        "result": "SRH won by 1 run"
    },
    {
        "M_no": "51st Match, (N) at Mumbai, May 3 2024",
        "vs": "(KKR vs MI)",
        "result": "KKR won by 24 runs"
    },
    {
        "M_no": "52nd Match, (N) at Bengaluru, May 4 2024",
        "vs": "(GT vs RCB)",
        "result": "RCB won by 4 wkts (38b rem)"
    },
    {
        "M_no": "53rd Match, (D/N) at Dharamsala, May 5 2024",
        "vs": "(CSK vs PBKS)",
        "result": "CSK won by 28 runs"
    },
    {
        "M_no": "54th Match, (N) at Lucknow, May 5 2024",
        "vs": "(KKR vs LSG)",
        "result": "KKR won by 98 runs"
    },
    {
        "M_no": "55th Match, (N) at Mumbai, May 6 2024",
        "vs": "(SRH vs MI)",
        "result": "MI won by 7 wkts (16b rem)"
    },
    {
        "M_no": "56th Match, (N) at Delhi, May 7 2024",
        "vs": "(RR vs DC)",
        "result": "DC won by 20 runs"
    },
    {
        "M_no": "57th Match, (N) at Hyderabad, May 8 2024",
        "vs": "(LSG vs SRH)",
        "result": "SRH won by 10 wkts (62b rem)"
    },
    {
        "M_no": "58th Match, (N) at Dharamsala, May 9 2024",
        "vs": "(RCB vs PBKS)",
        "result": "RCB won by 60 runs"
    },
    {
        "M_no": "59th Match, (N) at Ahmedabad, May 10 2024",
        "vs": "(CSK vs GT)",
        "result": "GT won by 35 runs"
    },
    {
        "M_no": "60th Match, (N) at Kolkata, May 11 2024",
        "vs": "(MI vs KKR)",
        "result": "KKR won by 18 runs"
    },
    {
        "M_no": "61st Match, (D/N) at Chennai, May 12 2024",
        "vs": "(RR vs CSK)",
        "result": "CSK won by 5 wkts (10b rem)"
    },
    {
        "M_no": "62nd Match, (N) at Bengaluru, May 12 2024",
        "vs": "(DC vs RCB)",
        "result": "RCB won by 47 runs"
    },
    {
        "M_no": "63rd Match, (N) at Ahmedabad, May 13 2024",
        "vs": "(KKR vs GT)",
        "result": "Match abandoned without a ball bowled"
    },
    {
        "M_no": "64th Match, (N) at Delhi, May 14 2024",
        "vs": "(LSG vs DC)",
        "result": "DC won by 19 runs"
    },
    {
        "M_no": "65th Match, (N) at Guwahati, May 15 2024",
        "vs": "(PBKS vs RR)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "66th Match, (N) at Hyderabad, May 16 2024",
        "vs": "(GT vs SRH)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "67th Match, (N) at Mumbai, May 17 2024",
        "vs": "(LSG vs MI)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "68th Match, (N) at Bengaluru, May 18 2024",
        "vs": "(CSK vs RCB)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "69th Match, (D/N) at Hyderabad, May 19 2024",
        "vs": "(PBKS vs SRH)",
        "result": "Starts at 15:30 local time"
    },
    {
        "M_no": "70th Match, (N) at Guwahati, May 19 2024",
        "vs": "(KKR vs RR)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "Qualifier 1, (N) at Ahmedabad, May 21 2024",
        "vs": "(TBA vs TBA)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "Eliminator, (N) at Ahmedabad, May 22 2024",
        "vs": "(TBA vs TBA)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "Qualifier 2, (N) at Chennai, May 24 2024",
        "vs": "(TBA vs TBA)",
        "result": "Starts at 19:30 local time"
    },
    {
        "M_no": "Final, (N) at Chennai, May 26 2024",
        "vs": "(TBA vs TBA)",
        "result": "Starts at 19:30 local time"
    }
]

    # items = item.objects.all()  # Query all items from the database
    
    return render(request, 'index.html', {'matches': json_data})

