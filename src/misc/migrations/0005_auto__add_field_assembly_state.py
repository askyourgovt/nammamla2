# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assembly.state'
        db.add_column(u'misc_assembly', 'state',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['misc.State']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Assembly.state'
        db.delete_column(u'misc_assembly', 'state_id')


    models = {
        u'misc.assembly': {
            'Meta': {'object_name': 'Assembly'},
            'end': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.State']"})
        },
        u'misc.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendance': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repRole': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.RepRole']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Representative']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Session']"})
        },
        u'misc.constituency': {
            'Meta': {'object_name': 'Constituency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'misc.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'misc.party': {
            'Meta': {'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name_l': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'misc.question': {
            'Meta': {'object_name': 'Question'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Representative']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Session']"})
        },
        u'misc.representative': {
            'Meta': {'object_name': 'Representative'},
            'all_time_attendance_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'all_time_no_questions_asked': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            'has_picture': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'})
        },
        u'misc.reprole': {
            'Meta': {'object_name': 'RepRole'},
            'assembly': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Assembly']"}),
            'constituency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Constituency']"}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'has_ec_affidavit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Party']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Representative']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Role']"}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'misc.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weightage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'misc.session': {
            'Meta': {'object_name': 'Session'},
            'assembly': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Assembly']"}),
            'average_member_attendance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'total_working_days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'misc.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['misc']