avatars ={
    "avatar1" : "https://www.w3schools.com/w3css/img_avatar.png",
    "avatar2" : "https://www.w3schools.com/w3css/img_avatar2.png",
    "avatar3" : "https://www.w3schools.com/w3css/img_avatar3.png",
    "avatar4" : "https://www.w3schools.com/w3css/img_avatar4.png",
    "avatar5" : "https://www.w3schools.com/w3css/img_avatar5.png",
    "avatar6" : "https://www.w3schools.com/w3css/img_avatar6.png"
}

def stakeholder_card(data):
    styling = """
    <style>
    p {
    border-color: red;
    border-bottom: 1px solid;
    }
    p:hover {
    color: darkorange;
    border-width: 3px;
    }
    .card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 60%;
    border-radius: 5px;
    }

    .card:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }

    img {
    border-radius: 5px 5px 0 0;
    }

    .container {
    padding: 2px 16px;
    }
    </style>
    """

    card = """
    <body style="padding:20px;">
    <h2>Stakeholder Card</h2>

    <div class="card">
    <img src={avatar} alt="Avatar" style="width:100%">
    <div class="container">
        <h2 style="padding:5px;text-align:center"><b>{name}</b></h2> 
        <p>Job Title: <b>{job_title}</b> </p>
        <p>Emial: <b>{email}</b> </p>
        <p>Company: <b>{company}</b> </p>
        <p>Address: <b>{address}</b> </p>
        <p>Post Code: <b>{post_code}</b> </p>
        <p>Phone Number: <b>{phone_number}</b> </p>
        <p>Employment Length: <b>{current_employment_length}</b> </p>
        <p>Current Start Date: <b>{employment_start_date}</b> </p>
        <p>URLs: <b>{URLs}</b> </p>
        <p>Tags: <b>{tags}</b> </p>
    </div>
    </div>

    </body>
    """.format(
        avatar=avatars[data['Avatar Number']], 
        name=data['Name'],
        job_title=data['Job Title'],
        email=data['Email'],
        company=data['Company'],
        address=data['Address'],
        post_code=data['Post Code'],
        phone_number=data['Phone Number'],
        current_employment_length=data['Current Employment Length'],
        employment_start_date=data['Employment Start Date'],
        URLs=data['URLs'],
        tags=data['Tags']
        )
    return(styling+card)