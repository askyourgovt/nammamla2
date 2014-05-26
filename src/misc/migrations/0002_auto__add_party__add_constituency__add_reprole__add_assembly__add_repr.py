# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Party'
        db.create_table(u'misc_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_name_l', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'misc', ['Party'])

        # Adding model 'Constituency'
        db.create_table(u'misc_constituency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'misc', ['Constituency'])

        # Adding model 'RepRole'
        db.create_table(u'misc_reprole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Representative'])),
            ('constituency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Constituency'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Party'])),
            ('assembly', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Assembly'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Role'])),
            ('start', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('has_ec_affidavit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'misc', ['RepRole'])

        # Adding model 'Assembly'
        db.create_table(u'misc_assembly', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('start', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'misc', ['Assembly'])

        # Adding model 'Representative'
        db.create_table(u'misc_representative', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=15)),
            ('birth_year', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('has_picture', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qualification', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=100)),
            ('all_time_attendance_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('all_time_no_questions_asked', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'misc', ['Representative'])

        # Adding model 'Attendance'
        db.create_table(u'misc_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Representative'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Session'])),
            ('repRole', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.RepRole'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('attendance', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=100)),
        ))
        db.send_create_signal(u'misc', ['Attendance'])

        # Adding model 'Session'
        db.create_table(u'misc_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('start', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('assembly', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Assembly'])),
            ('total_working_days', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('average_member_attendance', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'misc', ['Session'])

        # Adding model 'Role'
        db.create_table(u'misc_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_l', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('weightage', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'misc', ['Role'])


    def backwards(self, orm):
        # Deleting model 'Party'
        db.delete_table(u'misc_party')

        # Deleting model 'Constituency'
        db.delete_table(u'misc_constituency')

        # Deleting model 'RepRole'
        db.delete_table(u'misc_reprole')

        # Deleting model 'Assembly'
        db.delete_table(u'misc_assembly')

        # Deleting model 'Representative'
        db.delete_table(u'misc_representative')

        # Deleting model 'Attendance'
        db.delete_table(u'misc_attendance')

        # Deleting model 'Session'
        db.delete_table(u'misc_session')

        # Deleting model 'Role'
        db.delete_table(u'misc_role')


    models = {
        u'misc.assembly': {
            'Meta': {'object_name': 'Assembly'},
            'end': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
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
        u'misc.party': {
            'Meta': {'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name_l': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
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
        }
    }

    complete_apps = ['misc']