diff --git a/work.py b/work.py
index bcd08af..b3c4d46 100644
--- a/trytond/trytond/modules/project/work.py
+++ b/trytond/trytond/modules/project/work.py
@@ -188,13 +188,11 @@ class Work(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
         'get_total')
     comment = fields.Text('Comment')
     parent = fields.Many2One('project.work', 'Parent',
-        left='left', right='right', ondelete='RESTRICT',
+        ondelete='RESTRICT',
         domain=[
             ('company', '=', Eval('company', -1)),
             ],
         depends=['company'])
-    left = fields.Integer('Left', required=True, select=True)
-    right = fields.Integer('Right', required=True, select=True)
     children = fields.One2Many('project.work', 'parent', 'Children',
         domain=[
             ('company', '=', Eval('company', -1)),
@@ -219,14 +217,6 @@ class Work(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
         WorkStatus = pool.get('project.work.status')
         return WorkStatus.get_default_status(cls.default_type())

-    @classmethod
-    def default_left(cls):
-        return 0
-
-    @classmethod
-    def default_right(cls):
-        return 0
-
     @classmethod
     def __register__(cls, module_name):
         TimesheetWork = Pool().get('timesheet.work')
@@ -310,6 +300,12 @@ class Work(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
         # Migration from 5.4: replace state by status
         table_project_work.not_null_action('state', action='remove')

+        if table_project_work.column_exist('left'):
+            table_project_work.drop_column('left')
+
+        if table_project_work.column_exist('right'):
+            table_project_work.drop_column('right')
+
     @fields.depends('type', 'status')
     def on_change_type(self):
         pool = Pool()
