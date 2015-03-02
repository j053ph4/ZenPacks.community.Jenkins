
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.JenkinsBuildPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'JenkinsBuild',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "description"
                    }, 
                    {
                        "name": "getBuildStatus"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Description", 
                        "renderer": "pass_link", 
                        "id": "description", 
                        "dataIndex": "description"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Build Status", 
                        "renderer": "pass_link", 
                        "id": "getBuildStatus", 
                        "dataIndex": "getBuildStatus"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.JenkinsBuildPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('JenkinsBuildPanel', ZC.JenkinsBuildPanel);
    ZC.registerName('JenkinsBuild', _t('Jenkins Build'), _t('Jenkins Builds'));
    
    })();

