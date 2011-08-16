(function(){
    new TWTR.Widget({
        version: 2,
        type: 'profile',
        rpp: 5,
        interval: 6000,
        width: 250,
        height: 300,
        theme: {
            shell: {
                background: '#262626',
                color: '#d6dbdf'
                border: 2px solid #d6dbdf;
            },
            tweets: {
                background: '#262626',
                color: '#d6dbdf',
                links: '#ffbb00'
            }
        },
        features: {
            scrollbar: false,
            loop: false,
            live: true,
            hashtags: true,
            timestamp: true,
            avatars: false,
            behavior: 'all'
        }
    }).render().setUser('scharan').start();
}());
