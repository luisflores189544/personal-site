  

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
        selected_choice: 0,
        width_size: 0
    },
    delimiters: ["[%", "%]"],
    mounted() {
        this.$nextTick(function() {
            window.addEventListener('resize', this.getWindowWidth);

            this.getWindowWidth()

            
        })
    },
    methods: {
        anwserSelected: function (id) {
            if (this.selected_choice !== 0) {
                this.resetChoiceBtnBG(this.selected_choice)
            }
            this.selected_choice = id;

            if (this.width_size > 480) {
                this.clearSelected();

                let btn_id = document.getElementById(id);
                btn_id.innerText = 'X'
            };
            this.changeChoiceBtnBG(this.selected_choice)
            this.enableSubmitBtn();
        },

        clearSelected: function () {
            let choice_btn = document.getElementsByClassName('training-answer-btn');
            console.log('clearSelected',choice_btn)
            let i;
            for (i = 0; i <choice_btn.length; i++) {
                choice_btn[i].innerText = ''
            };
        },

        enableSubmitBtn: function() {
            let btn = document.getElementById('training-submit-btn');
            btn.disabled = false;
        },

        getWindowWidth(event) {
            this.width_size = document.documentElement.clientWidth;

            console.log('getWindowWidth', this.width_size)
            if (this.width_size <= 480) {
                console.log('show execute addChoiceToBtn')
                this.addChoiceToBtn()
            } else {
                this.clearSelected()
            }
        },

        addChoiceToBtn: function() {
            let choice_btn = document.getElementsByClassName('training-answer-btn');
            let choice_text = document.getElementsByClassName('col-form-label');
            let i;
            for (i = 0; i <choice_btn.length; i++) {
                choice_btn[i].innerText = choice_text[i].innerText
            }

        },

        changeChoiceBtnBG: function(id) {
            let btn_id = document.getElementById(id);
            btn_id.setAttribute("style", "background-color:green;")
        },

        resetChoiceBtnBG: function(id) {
            let btn_id = document.getElementById(id);
            btn_id.setAttribute("style", "background-color:#007bff;")
        }
    }
    
})





