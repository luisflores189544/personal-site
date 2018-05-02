  

new Vue({
    el:'#vue-navbar',
    
    data: {
        navbar_links:{
            home:false,
            projects:false,
            about_me:false
        },
        nav_names:{
            home:'Home',
            apps: ['Training Session', 'App2', 'App3'],
            about_me:'About Me',
            architecture:'Site Architecture'
        }
    },
    delimiters: ["[%", "%]"],

    methods: {
        setNavBarToActive:function(name){
            this.setNavBarToInactive()
        },

        setNavBarToInactive:function(){
            this.navbar_links['home'] = false,
            this.navbar_links['projects'] = false,
            this.navbar_links['about_me'] = false
        }
    }
});


new Vue({
    el:'#vue-training',
    data: {
        title:'Training Session',
        session_required_title: 'Training Required',
        session_past_due_title: 'Training Past Due',
        test:''
    },
    delimiters: ["[%", "%]"],
})

new Vue({
    el:'#vue-training-session',
    data: {
        selected_choice:''
    },
    delimiters: ["[%", "%]"],
    methods: {
        anwserSelected: function (id) {
            choice_id = id;
            this.selected_choice = choice_id;

            this.clearSelected();
            this.enableSubmitBtn();

            let btn_id = document.getElementById(id);
            btn_id.innerText = 'X'

        },

        clearSelected: function () {
            let choice_btn = document.getElementsByClassName('training-answer-btn');
            console.log(choice_btn)
            let i;
            for (i = 0; i <choice_btn.length; i++) {
                choice_btn[i].innerText = ''
            };
            
        },

        enableSubmitBtn: function() {
            let btn = document.getElementById('training-submit-btn');
            btn.disabled = false;
        }
    }
    
})





